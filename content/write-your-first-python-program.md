Title: Write your first Python program
Date: 2019-01-01 04:00
Tags: python-for-everyone, vs-code, atom
image_url: /images/patagonia_5_orig.jpg

# Background
<!-- PELICAN_BEGIN_SUMMARY -->
In the last post, we ran some very basic python code directly in a python interactive session. But what would a more realistic example of python code look like? To make our lives easier, the most basic thing we need is a text editor (not a word processor). This will allow us to write and save python code as a file with a `.py` file extension (e.g. `example_script.py`).
<!-- PELICAN_END_SUMMARY -->

# Pick a text editor
We could just use `Notepad` on Windows, `TextEdit` on Mac or the built in editor on Linux. But there are fancier text editors out there that use syntax highlighting and formatting to make it easier to read our code. Choose whatever text editor you want. 

Two free, cross-platform options are VS Code and Atom. VS Code was created by Microsoft. Atom was created by Github, which is now owned by Microsoft. To be extra confusing and hip, I currently use [VS Codium](https://vscodium.com/). 

If you don't care (you shouldn't), download and install [VS Code](https://code.visualstudio.com/). Then install the Python Extension for VS Code, to get syntax highlighting and other useful tools.

# Create a `.py` file
Once you have a text editor installed, open it and create a new file. Save it with the `.py` file extension. When choosing a filename, I recommend keeping it short, and all lowercase. Use underscores if it improves readability (e.g. `example_script.py` is preferred, as opposed to `examplescript.py` or `Example Script.py`). I'll call mine `my_first.py`. You can save it wherever you want.

# Stay organized
To stay organized, I recommend the following folder structure. Pick a location that you want to save all your scripts (e.g. your local home folder, `/home/yourname` in Linux, `C:\Users\yourname\` on Windows, or a folder on a network drive that gets backed up).

Now create a new folder in that location named `repos`. Repos is short for Repositories, and this folder structure will be useful when we talk about `git` (in the future). Within `repos` create another folder named `python-examples`. The folder path will now look something like `C:\Users\user\repos\python-examples`. By the way, I will use the words *folder* and *directory* interchangeably.

Save or copy `my_first.py` into `python-examples` for now. Open `my_first.py` and copy-paste the following lines:

```python
x = 1
y = 2
z = x + y
print(z)
```
Save `my_first.py`.

# Run `my_first.py`
Open the command line. At this point, we can run `my_first.py` a couple of different ways. 

The first option does not require us to change the command line to the `python-examples` directory. Type `python` **with a space after it** and drag `my_first.py` onto the command line. This will copy the full path to the file. If you hit enter, the code in `my_first.py` will run.

For the second option, we need to `cd` into the `python-examples` directory. If you don't know what that means, give it a quick google. After you `cd` into the same directory as `my_first.py`, you can simply type `python my_first.py` and hit enter.

The important takeaway is that `python` needs to know exactly where the file is located before it can run it. That means you can either tell it the *absolute* path of the file, OR you can move the command line to where the file is located and tell python the *relative* path to the file.
