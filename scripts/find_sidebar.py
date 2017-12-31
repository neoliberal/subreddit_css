"""finds sidebar name and height"""
from pathlib import Path

import sass

def _sidebar_path() -> Path:
    sidebar_dir = (Path(__file__).parents[1] / "assets" / "sidebar")
    return next((
        image for image in sidebar_dir.glob("*.png")
        if not image.name.startswith('_')
    ), None)

def custom_sidebar_exists() -> bool: 
    """checks if sidebar image actually exists"""
    return _sidebar_path() is not None

def custom_sidebar_dimensions() -> sass.SassList:
    """returns height of sidebar"""
    from PIL import Image

    sidebar_path: Path = _sidebar_path()
    return sass.SassList(
        [sass.SassNumber(dim, unit="px") for dim in Image.open(sidebar_path).size],
        separator=sass.SASS_SEPARATOR_COMMA
    )

def custom_sidebar_name() -> str:
    """returns name of sidebar"""
    sidebar_path: Path = _sidebar_path()
    return sidebar_path.stem

if __name__ == "__main__":
    print(custom_sidebar_name())
    print(custom_sidebar_dimensions())
