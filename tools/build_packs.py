"""Build separate Minecraft data and resource pack archives."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import json


ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
VERSION = "26.3"
SOURCE_SUFFIXES = {".af", ".bbmodel", ".psd", ".xcf"}


def add_tree(archive: ZipFile, directory: Path) -> None:
    if not directory.exists():
        return
    for path in sorted(directory.rglob("*")):
        if path.is_file() and path.suffix.lower() not in SOURCE_SUFFIXES:
            archive.write(path, path.relative_to(ROOT).as_posix())


def build(kind: str) -> Path:
    output = DIST / f"PocketDimensions-{VERSION}-{kind}.zip"
    metadata = ROOT / ("pack.mcmeta" if kind == "data" else "resource_pack.mcmeta")
    json.loads(metadata.read_text(encoding="utf-8"))

    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        archive.write(metadata, "pack.mcmeta")
        archive.write(ROOT / "pack.png", "pack.png")
        add_tree(archive, ROOT / ("data" if kind == "data" else "assets"))
        add_tree(archive, ROOT / "1_21_10" / ("data" if kind == "data" else "assets"))
        if kind == "data":
            add_tree(archive, ROOT / "pre_26_3" / "data")

    with ZipFile(output) as archive:
        assert archive.testzip() is None
    return output


if __name__ == "__main__":
    DIST.mkdir(exist_ok=True)
    for pack_kind in ("data", "resource"):
        print(build(pack_kind))
