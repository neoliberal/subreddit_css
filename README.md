# /r/Neoliberal CSS

SASS source for the r/neoliberal theme, plus some additional scripts and assets related to the subreddit styling.

Based off the [Structura](https://www.reddit.com/r/Structura/) subreddit theme.

## Compiling the CSS

(The actual commands you use may differ slightly based on your OS/environment/whatever)

* First, create a virtual environment: `python3 -m venv env`
* Install the required python modules with: `pip3 install -r requirements.txt`
* Compile the CSS: `python3 compile.py`
* Copy output.css to the [subreddit stylesheet](https://www.reddit.com/r/neoliberal/about/stylesheet)
