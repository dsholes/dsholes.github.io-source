Title: Writing your first Python program
Date: 2019-01-01 04:00
Tags: python, quick-start, beginner, program
image_url: /images/generic1.jpg

In the last post, we ran some very basic python code directly in a python interactive session. But what would a more realistic example of python code look like? To make our lives easier, the most basic thing we need is a text editor (not a word processor). This will allow us to write and save python code as a file with a `.py` file extension (e.g. `example_script.py`).

We could just use `Notepad` on Windows, `TextEdit` on Mac or the built in editor on Linux. But there are fancier text editors out there that use syntax highlighting and formatting to make it easier to read our code. Choose whatever text editor you want. I wanted something free, open source and cross platform, so I chose [Atom](https://atom.io/). See [this post](link to article on installing Atom) for instructions on installing and configuring Atom.

Once you have a text editor installed, open it and save the new file as whatever you want it to be called. However, I recommend making it all lowercase, and not using spaces. I'll call mine `example.py`. You can save it wherever you want. To stay organized, I recommend the following folder structure.

Pick a location that you want to save all your scripts (e.g. a folder on a server that gets backed up, or your local home folder, `/home/user` in Linux, `C:\Users\user\` on Windows). Now create a new folder in that location named `repos`. Repos is short for Repositories, and this folder structure will be useful when we talk about `git` [in the future](link to article on git). Within `repos` create another folder named `python-examples`. Save or copy `example.py` here for now. The folder path will now look something like `C:\Users\user\repos\python-examples`.


```python
import numpy as np

x = 1
y = 2
z = x + y

class MyNewThing:
    def __init__(stuff):
        return

def my_func(a):
    return a + 1

my_arr = np.linspace(0, 100, 20)
```
