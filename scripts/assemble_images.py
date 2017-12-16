"""turns flairs into spritesheets"""
#!usr/bin/python3.6
from pathlib import Path
from typing import List, Tuple

def assemble_images() -> None:
    """
    converts flairs into a combined flairsheet
    """
    flairs_dir: Path = (Path.cwd().parent / "assets" / "flairs")
    for subdir in [dir for dir in flairs_dir.iterdir() if dir.is_dir()]:
        assemble_spritsheet(subdir)
    return

def assemble_spritsheet(flair_dir: Path) -> None:
    """
    assembles the spritsheet from various images

    stolen from https://gist.github.com/gourneau/939252
    """
    from PIL import Image

    individual_image: Tuple[int, int] = (92, 100)

    images: List[Image] = [
        Image.open(image).resize(individual_image)
        for image in flair_dir.glob("_*.png") # individual images must be underscored
    ]

    spritesheet: Image = Image.new(
        mode="RGBA",
        size=(individual_image[0], individual_image[1] * len(images)),
        color=(0, 0, 0, 0)
    )

    for count, image in enumerate(images):
        location: int = individual_image[1] * count
        spritesheet.paste(image, (0, location))

    # for example, if the folder name is "politicians"
    # the image will be saved as "politicians_spritesheet.png" in the politicians folder
    spritesheet.save(flair_dir / (flair_dir.name + "-flairs.png"))
    return
