"""compiles sass with custom functions"""
from pathlib import Path

import sass

from source.detail.add_images import custom_flair_images

def compile_sass() -> str:
    """compiles sass index file"""
    index_file: Path = (Path(__file__).resolve().parent / "index.scss")
    return sass.compile(
        filename=str(index_file),
        custom_functions={
            custom_flair_images
        }
    )

def main() -> None:
    """outputs generated css to file"""
    output: Path = (Path(__file__).resolve().parent / "output.css")
    output.touch()
    with output.open("w") as f:
        f.write(compile_sass())
    # fix donation_spring2018 image name, and remove charset
    with open(output, "r") as f:
        new_css = f.read()
        new_css = new_css.replace(
            "%%donation_spring2018-flair%%", "%%donation-spring2018-flair%%"
        )
        new_css = new_css.replace('@charset "UTF-8";\n', '')
    with open(output, "w") as f:
        f.write(new_css)

if __name__ == "__main__":
    main()
