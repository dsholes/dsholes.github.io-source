Title: Install Python on your computer
Date: 2019-11-30 23:00
Tags: python-for-everyone, install, miniconda, anaconda, conda
image_url: /images/patagonia_2_orig.JPG

# Background
<!-- PELICAN_BEGIN_SUMMARY -->
Before you can run any Python code, you have to install a Python interpreter on your computer. The interpreter is what reads, translates, and executes your Python code (which is just a text file with a `.py` extension). At this point that's the most you need to know. Don't get bogged down in the technical jargon for now.
<!-- PELICAN_END_SUMMARY -->

Python, like any language or piece of software, is constantly evolving, so there are a bunch of versions floating around. There are a few differences between Python 2 and Python 3. I recommend you learn Python 3. The latest version distributed with Miniconda as of August 2019 is Python 3.7.

Because Python is open source, there are many people/organizations that offer **[distributions](https://www.infoworld.com/article/3267976/anaconda-cpython-pypy-and-more-know-your-python-distributions.html)** of it. We'll use the Anaconda distribution. I use the Anaconda distribution (specifically Miniconda) because it uses the package manager `conda`, which allows you to easily install Python packages, as well as create and manage Python environments. We'll discuss what those are and why that's valuable later. For now, let's just get to the good stuff.

# Download and install `miniconda`
- Go to the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html)
- Download the installer for the latest version of Python 3 for your operating system (Windows, macOS or Linux) and [CPU architecture](https://support.microsoft.com/en-us/help/15056/windows-32-64-bit-faq) (32 vs 64-bit).
- Follow the instructions on the installer. For detailed instructions, see [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

**Windows Tip**: Make sure you allow the installer to add Python to your PATH environment variable, and install the single user version (especially if you don't have Admin rights on your machine).

# Test that it worked
Open the command line. On Windows open the `Command Prompt`, and on macOS open `Terminal`.

- Type `conda info`.

    ![conda-test-install]({static}images/conda_test_install.PNG)
    
- Type `python`.

    ![python-test-install]({static}images/python_test_install.png)

# Issues?
Hopefully, the two commands above didn't produce any error messages. If they did, copy-paste the message into Google. You will find the answer ;).

If you get a message like `python` or `conda` command not recognized, then you most likely need to add your miniconda3 installation to your system Path.

By the way, learning a bit about the command line (Terminal/PowerShell) will be helpful as you start programming more. If you're interested in some details you can read this [primer for command line](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/command-line-101).  

Hopefully that wasn't too painful, and everything worked as expected. Let's [run your first Python code]({filename}run-your-first-python-code.md).
