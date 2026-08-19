#!/usr/bin/env python3
"""Content-addressed snapshot of a fetched URL.

Usage:
    python3 snapshot.py URL [URL ...]
    python3 snapshot.py --selftest

Fetches each URL, stores the response body under store/<sha256>.<ext>,
and appends a row to INDEX.md. The hash is of the exact bytes stored.
Closes the method gap registered in falsifiers/adjudications/
CITATION-AUDIT-2026-08-19.md for all work from 2026-08-20 onward.
Existing citations are deliberately not retrofitted.
"""

import hashlib
import mimetypes
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
STORE = HERE / "store"
INDEX = HERE / "INDEX.md"
UA = "Mozilla/5.0 (X11; Linux x86_64) research-snapshot/1.0"

INDEX_HEADER = (
    "# Snapshot index -- content-addressed fetch records\n\n"
    "Appended by `snapshot.py`. Never edited by hand. One row per fetch;\n"
    "re-fetching a changed page appends a new row rather than replacing one.\n\n"
    "| Fetched (UTC) | URL | sha256 | Bytes | File |\n"
    "|---|---|---|---|---|\n"
)


def snapshot(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read()
        ctype = resp.headers.get_content_type()
    digest = hashlib.sha256(body).hexdigest()
    ext = mimetypes.guess_extension(ctype) or ".bin"
    if ext == ".htm":
        ext = ".html"
    STORE.mkdir(exist_ok=True)
    fname = digest + ext
    (STORE / fname).write_bytes(body)
    if not INDEX.exists():
        INDEX.write_text(INDEX_HEADER)
    when = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    with INDEX.open("a") as f:
        f.write(f"| {when} | {url} | `{digest}` | {len(body)} | `store/{fname}` |\n")
    return digest


def selftest() -> None:
    # ponytail: hash correctness only; network path is exercised by real use
    known = hashlib.sha256(b"abc").hexdigest()
    assert known == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    assert (mimetypes.guess_extension("application/pdf")) == ".pdf"
    print("selftest ok")


def ingest(path: str, url: str, ctype: str = "application/octet-stream") -> str:
    """Register bytes already fetched by another client (e.g. curl, for hosts
    urllib cannot reach). The hash is still of the exact bytes stored; the
    fetch client is the only difference from snapshot()."""
    body = Path(path).read_bytes()
    digest = hashlib.sha256(body).hexdigest()
    ext = mimetypes.guess_extension(ctype) or ".bin"
    if ext == ".htm":
        ext = ".html"
    STORE.mkdir(exist_ok=True)
    fname = digest + ext
    (STORE / fname).write_bytes(body)
    if not INDEX.exists():
        INDEX.write_text(INDEX_HEADER)
    when = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    with INDEX.open("a") as f:
        f.write(f"| {when} | {url} | `{digest}` | {len(body)} | `store/{fname}` |\n")
    return digest


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--selftest":
        selftest()
        sys.exit(0)
    if sys.argv[1] == "--ingest":
        print(ingest(sys.argv[2], sys.argv[3], *sys.argv[4:5]))
        sys.exit(0)
    for u in sys.argv[1:]:
        print(snapshot(u), u)
