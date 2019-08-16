Title: Installing Python on your computer
Date: 2019-01-01 02:00
Tags: python, quick-start, install, miniconda, anaconda, conda
image_url: /images/generic1.jpg

Before you can run any Python code, you have to install a Python interpreter on your computer. The interpreter is what reads your Python code, and translates it into "lower level"  machine code that your computer can then understand and execute (**verify this**). At this point that's the most you need to know. Don't get bogged down in the technical jargon for now.

Python, like any software, is constantly evolving, so there are a bunch of versions floating around. There are a few differences between Python 2 and Python 3. I recommend you learn Python 3. The latest version as of **PUT-DATE-HERE** is Python 3.7 (verify this).

Because Python is open source, there are many people/organizations that offer **distributions (link to description of 'distribution')** of it. We'll use the Anaconda distribution. Anaconda is (**insert description here**)... I use the Anaconda distribution (specifically Miniconda) because it uses the package manager `conda`, which allows you to easily install Python packages (**describe what these are**), as well as create and manage Python environments. We'll discuss why that's valuable later. For now, let's just get to the good stuff.

1. Download Miniconda
    - Go to [Miniconda webpage](link to Miniconda)
    - Pick the latest version for your operating system (Windows, MacOS or Linux)
    - Click the download link
2. Follow the instructions on the installer. For detailed instructions, see [here](link to miniconda install instructions). Make sure to add it to Windows Path, and install the single user version (especially if you don't have Admin rights on your machine).
3. Test that it worked
    - What's a good test?
    - Open Terminal or command prompt
        - Link to article on Terminal/Command Prompt 101. Don't fear the Terminal
    - Type `conda info`
    - Type `python`

Hopefully that wasn't too painful, and everything worked as expected. Let's [write our first Python code](link to next article).
