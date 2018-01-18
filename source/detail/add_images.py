"""sass custom hook to add images"""
from pathlib import Path
from typing import Tuple, List

import sass

def custom_flair_images() -> sass.SassMap:
    """reads directory and produces a map of flairs"""
    flairs_dir: Path = (Path(__file__).resolve().parents[2] / "assets" / "flairs")

    return sass.SassMap({
        subdir.name: flairs_list(subdir)
        for subdir in (
            dir for dir in flairs_dir.iterdir()
            if dir.is_dir() and not dir.stem.startswith('_')
        )
    })

def flairs_list(flair_dir: Path) -> sass.SassList:
    """creates flair list"""
    flairs: List[Path] = sorted(list(flair_dir.glob("_*.png")))
    assemble_spritsheet(flair_dir, flairs)
    return sass.SassList(
        [
            flair.stem[1:]
            for flair in flairs
        ],
        separator=sass.SASS_SEPARATOR_COMMA
    )

def assemble_spritsheet(flair_dir: Path, flairs: List[Path]) -> None:
    """
    assembles the spritsheet from various images

    stolen from https://gist.github.com/gourneau/939252
    """
    from PIL import Image

    individual_image: Tuple[int, int] = (92, 100)
    images: List[Image] = [
        Image.open(flair).resize(individual_image)
        for flair in flairs
    ]

    spritesheet: Image = Image.new(
        mode="RGBA",
        size=(individual_image[0], individual_image[1] * len(images)),
        color=(0, 0, 0, 0)
    )

    for count, image in enumerate(images):
        location: int = individual_image[1] * count
        spritesheet.paste(image, (0, location))

    # reduce the output file's colour depth
    alpha = spritesheet.split()[-1]
    spritesheet = spritesheet.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
    spritesheet.paste(255, mask)

    # for example, if the folder name is "politician"
    # the image will be saved as "politician-flair.png" in the "politician" folder
    spritesheet.save(flair_dir / f"{flair_dir.name}-flair.png", transparency=255)
    return

if __name__ == "__main__":
    print(custom_flair_images())
