#!/usr/bin/env python3
"""Build the portable skill ZIP using only the Python standard library."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "piszpoludzku"


def main():
    parser = argparse.ArgumentParser(description="Zbuduj paczkę Pisz po ludzku.")
    parser.add_argument("--output", type=Path, default=ROOT / "dist/piszpoludzku.zip")
    args = parser.parse_args()
    files = {
        path.relative_to(SOURCE).as_posix(): path
        for path in SOURCE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix not in (".pyc", ".pyo")
    }
    files.update({name: ROOT / name for name in ("LICENSE", "VERSION")})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.output, "w") as archive:
        for name, path in sorted(files.items()):
            entry = ZipInfo("piszpoludzku/" + name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes().replace(b"\r\n", b"\n"))
    print(f"Paczka: {args.output} ({len(files)} plików)")


if __name__ == "__main__":
    main()
