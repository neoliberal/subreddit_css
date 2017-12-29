"""splits spritesheet into individual images"""
from typing import Tuple

def spritesheet_to_image(image: str) -> None:
    """main"""
    from PIL import Image
    spritesheet: Image.Image = Image.open(image)
    width, height = spritesheet.size
    new_image_height: int = 100

    number: int = int(height / new_image_height)
    print(number)
    for i in range(0, number):
        box: Tuple[int, int, int, int] = (
            0,
            new_image_height * i,
            width,
            new_image_height * (i+1)
        )
        print(box)
        sprite: Image = spritesheet.crop(box)
        sprite.save(f"{i}.png")
    return

if __name__ == "__main__":
    import sys
    spritesheet_to_image(sys.argv[1])
