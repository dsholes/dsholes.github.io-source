Title: Run your first Python code
Date: 2019-11-30 22:00
Tags: python, python-for-everyone
image_url: /images/patagonia_1_orig.JPG

# Background
<!-- PELICAN_BEGIN_SUMMARY -->
At this point you have successfully [installed Python on your computer]({filename}install-python-on-your-computer.md) using the Miniconda distribution. You're ready to run some Python code.
<!-- PELICAN_END_SUMMARY -->

If you've programmed before, you may want to skip this and go straight to "[Write your first Python program]({filename}write-your-first-python-program.md)". If you're wondering what python code looks like, then read below.

The most basic way to write/run python code is using the python interpreter directly from Terminal/Command Prompt.

# The Steps

1. Open Terminal/Command Prompt
2. Type `python`, to start the python interpreter
    - Your terminal should now look something like this:

    ![python-interpreter-1]({static}images/run_first_python_interpreter_1.PNG)

3. Type `x = 1` and hit enter
    - You've just run your first python code!! Pretty anti-climactic, huh? It may seem like nothing happened. What you've done is created a variable `x` and stored the integer `1` in that variable.

    ![python-interpreter-2]({static}images/run_first_python_interpreter_2.PNG)

4. Type `y = 2` and hit enter
    ![python-interpreter-3]({static}images/run_first_python_interpreter_3.PNG)

5. Type `z = x + y` and hit enter
    - As I said in the intro article, if you understand basic algebraic concepts, then you can learn python. If `x = 1` and `y = 2`, what does `z` equal?

    ![python-interpreter-4]({static}images/run_first_python_interpreter_4.PNG)

6. To see what `z` is now storing, type `print(z)` and hit enter. Alternatively, you can just type `z` and hit enter. Your terminal should now look like this:

    ![python-interpreter-5]({static}images/run_first_python_interpreter_5.PNG)

You've run your first python code! See, not so scary. One thing you may notice is there's no way to save the code that you've just written.

In the next post, we'll cover a more realistic/useful way to write, save and execute python code.
