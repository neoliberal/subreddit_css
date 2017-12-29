"""sass custom hook to add images"""
from pathlib import Path

import sass

def flair_images() -> sass.SassMap:
    flairs_dir: Path = (Path.cwd().parent / "assets" / "flairs")

    return sass.SassMap({
        subdir.name: flairs_list(subdir)
        for subdir in (dir for dir in flairs_dir.iterdir() if dir.is_dir())
    })

def flairs_list(flair_dir: Path) -> sass.SassList:
    return sass.SassList(
        [
            flair.stem[1:]
            for flair in sorted(
                list(flair_dir.glob("_*.png")),
                key=lambda image: str(image.name)
            )
        ],
        separator=sass.SASS_SEPARATOR_COMMA
    )

if __name__ == "__main__":
    print(flair_images())
