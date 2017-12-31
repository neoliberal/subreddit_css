"""sass custom hook to add images"""
from pathlib import Path

import sass

def custom_flair_images() -> sass.SassMap:
    """reads directory and produces a map of flairs"""
    flairs_dir: Path = (Path(__file__).parents[1] / "assets" / "flairs")

    return sass.SassMap({
        subdir.name: flairs_list(subdir)
        for subdir in (
            dir for dir in flairs_dir.iterdir()
            if dir.is_dir() and not dir.stem.startswith('_')
        )
    })

def flairs_list(flair_dir: Path) -> sass.SassList:
    """creates flair list"""
    return sass.SassList(
        [
            flair.stem[1:]
            for flair in sorted(
                list(flair_dir.glob("_*.png"))
            )
        ],
        separator=sass.SASS_SEPARATOR_COMMA
    )

if __name__ == "__main__":
    print(custom_flair_images())
