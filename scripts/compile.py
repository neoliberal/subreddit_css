from pathlib import Path

import sass

from add_images import custom_flair_images

def compile_sass() -> str:
    """compiles sass index file"""
    index_file: Path = (Path.cwd().parent / "index.scss")
    return sass.compile(
        filename=str(index_file),
        custom_functions={custom_flair_images}
    )

def main() -> None:
    """outputs generated css to file"""
    output: Path = (Path.cwd().parent / "output.css")
    output.touch()

    with output.open("w") as file:
        file.write(compile_sass())

if __name__ == "__main__":
    main()
