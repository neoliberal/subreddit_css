from pathlib import Path

import sass

from add_images import flair_images

def main() -> str:
    index_file: Path = (Path.cwd().parent / "index.scss")
    return sass.compile(
        filename=str(index_file),
        custom_functions={flair_images}
    )

if __name__ == "__main__":
    print(main())
