# /r/Neoliberal CSS

SASS source for the r/neoliberal theme, plus some additional scripts and assets related to the subreddit styling.

Based off the [Structura](https://www.reddit.com/r/Structura/) subreddit theme.

## Compiling the CSS

(The actual commands you use may differ slightly based on your OS/environment/whatever)

* First, create a virtual environment: `python3 -m venv env`
* Install the required python modules with: `pip3 install -r requirements.txt`
* Compile the CSS: `python3 compile.py`
* Copy output.css to the [subreddit stylesheet](https://www.reddit.com/r/neoliberal/about/stylesheet)

## Adding a Flair

Flairs must be pngs with a transparent background, have a width of 92px, and a height of 100px.

To add them to the CSS, simply copy the image into the appropriate directory in `./assets/flairs/$DIR`, and compile. Note that the filename must begin with an underscore, followed by alphanumeric characters and hyphens (ie. don't use underscores in flair names).

After compiling, there will be a new spritesheet in $DIR containing all the image flairs for that directory. Go to the [subreddit stylesheet](https://www.reddit.com/r/neoliberal/about/stylesheet), delete the old image (eg. philosopher-flair), and upload the new one, using the same name. You will also need to save the CSS, even if you didn't make any changes, to apply the new flair.

### Emoji Flairs

To make the image flair work on New Reddit and mobile, you will need to add the image to the subreddit emoji list. This list can be found [here](https://new.reddit.com/r/neoliberal/about/emojis). However, to make things easier, I've created a script that will automatically upload all missing flairs, called `deploy_emoji.py`. To run this, simply execute `python3 deploy_emoji.py`. You will be prompted to input "1" or "2" depending on whether you want to deploy to /r/Neoliberal or /r/Wumbotarian.

## Editing a User's Flair

See [this page](https://www.reddit.com/r/neoliberal/about/flair/) to edit a user's flair. There are two parts: the flair text, and the flair CSS. The CSS is a list of classes applied to the user flair, separated by spaces. The order of these classes doesn't matter. For an image flair, you need to include "image", "$DIR" and "$IMAGE-NAME". For example, "image centralbanker bernanke".

Text flairs are a bit more complicated. By default (ie. no CSS classes), the text flair will be invisible on Old Reddit, however it will appear on New Reddit and mobile. When an image flair has been applied, then the text will appear when you hover over the image on Old Reddit (New Reddit / mobile ignore CSS entirely so are unchanged).

To make the text flair appear on old reddit, you need to include "text" "$COLOR" and optionally "$COLOR-border" to the css. So a plain blue text flair would need the class "text blue". To add a red border (indicating the user is a moderator), the css should be "text blue red-border".

### Emoji Flairs

If the appropriate emoji has been uploaded to the [subreddit emoji list](https://new.reddit.com/r/neoliberal/about/emojis) then it can be added to a user's flair text. For example, to add a Bernanke emoji, add ":bernanke:" to the beginning of the users flair text.

## Imagebar

The Imagebar is the three images with overlayed text directly below the header on old reddit. I've called this the headerbar elsewhere, but I'll hopefully fix that at some point.

I'm in the process of automating a way to add these to the New Reddit sidebar. Hopefully that works alright.

### Changing an Image

Images may be jpeg or png, but must be 790px in width, and 112px in height. The sides of the image get cropped off on smaller screens, so ensure it looks good when cropped to 600px. I've found that the best-looking images have a single figure or thing on the right in the foreground, with a blurry background. This keeps the image from being too "noisy" and making it difficult to read the text or determine what the subject is.

Once you have an image, you just need to go to the [subreddit stylsheet](https://www.reddit.com/r/neoliberal/about/stylesheet), delete the old image, upload the new one using the same name, and save the CSS.

By far the most difficult part of this process is finding an image that works at the extreme aspect ratio we have. Using Google's [advanced image search](https://www.google.com/advanced_image_search) and selecting a "panoramic" aspect ratio can help.

### Changing the Text

The text for the imagebar buttons can be found in `./source/_manual.scss`, stored in "content:" properties. Simply edit the CSS, compile, and deploy as normal. These may be moved to a separate "var" file at some point to make editing easier for non-techmods.

### Changing the Link

This is where things get a bit weird. The links are actually stored in the sub's sidebar, which can be accessed via "Subreddit Settings" or [here](https://www.reddit.com/r/neoliberal/about/edit/). The CSS assumes that the first header in the sidebar (a line prefixed with a "#") is the imagebar. Each image is actually an image and a text-less link. For example:

    [](#headerbutton)[](https://www.google.com/)
    
To change the link, simply replace the URL and save. But be careful, as there is no way to undo this change (unlike changes to the stylesheet).
