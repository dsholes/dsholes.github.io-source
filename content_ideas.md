TO DO:
1. Change circle headshot on `About` page to be different from splash.
2. Make one `My Python Setup` article to make it easy to set up python on new machines with same conda/jupyterlab/vscode/git settings.
    1. Miniconda
        1. Path variables:
            1. `C:\Users\Sholes\AppData\Local\Continuum\miniconda3\Scripts`
            2. `C:\Users\Sholes\AppData\Local\Continuum\miniconda3`
            3. Might have to add to both user and system
    2. VSCode
        1. Disable telemetry
        2. Install python extension and 
        3. Change settings.json 
    3. Jupyterlab and nb_conda_kernels
        1. `conda install -c conda-forge jupyterlab`
        2. `conda install nb_conda_kernels`
        3. Add jupyter_notebook_config.py with correct terminal
    4. Add conda env (e.g. pydata) with pandas, numpy, plotly, seaborn and matplotlib
    4. Git
3. Finish all articles in `content`. Right now some are saved as `status=draft`.
4. Useful for turning jupyter notebooks into markdown/html without input: https://medium.com/capital-fund-management/automated-reports-with-jupyter-notebooks-using-jupytext-and-papermill-619e60c37330
    1. Use newest version of jupyterlab and nbconvert

Python:
1. Installing Python on Your Computer
    1. Miniconda - Why and how to use `conda`
2. Writing your first Python code
    1. Getting comfortable with Terminal/Command Prompt
3. Writing your first Python program
    1. Installing a Text Editor - VSCode or Atom
        1. Copy the following settings on every computer/platform that you use: `C:\Users\Sholes\AppData\Roaming\VSCodium\User\settings.json`
    2. What does a Python program look like (and what makes programming so useful)?
        1. Syntax - why is it important?
        2. Idea of data types (e.g. str, float, int, list, dict)
        3. `for` and `while` loops
        4. `if` statements and True/False booleans
    3. Using `conda` to install packages
    4. Version control with Git
        1. Change `.gitconfig` to use `vscodium` as editor:
            `git config --global -e`
        2. Add this to `.gitconfig`:
            ```
            [core]
                editor = codium --wait
            [user]
                name = Darren Sholes
                email = sholesdarren@gmail.com
           ```
4. Interacting with Excel or CSV data in Python with Pandas
    1. Interactive Python - Jupyterlab
    2. Reading table data with `pandas`
    3. Plotting data
        1. `matplotlib` for static plots
        2. `plotly` for interactive plots
        3. `seaborn` for styling and color management
5. Doing some serious maths with NumPy and SciPy
    1. Emphasize vectorizing for speed
    2. Matrix/vector operations
    3. Solving ode's
    4. Fourier transform
        1. Vibration data
6. Getting started with Geospatial Data Analysis in Python
    - Kaggle kernel winner
7. Getting started with Astrodynamics in Python
    - Sat passes with Skyfield
    - Sun vector with Poliastro
8. Getting started with Image Processing in Python
    - Flame position
9. Getting started with Music Processing in Python
    - Find delay between recordings
10. Interacting with AutoDesk Inventor in Python

Notes:
What else to put on website?
1. Recording an album with old smart phones...
    1. Download recorder app if one isn't pre-installed
    2. Change settings to highest quality (wav, sampling rate, etc)
    3. Cell phone placement and checking for peaking.
    4. "Clap" or snare hits to match up tracks
        1. Can also use python code to help (link to Getting started
            with Music Processing in Python)
    5. Mix everything in Reaper
        1. EQ
            1. Parametric ReaEQ to eliminate hissing and resonance
            2. Low pass filters to remove snare buzzing
        2. ReaFIR to eliminate noise
        3. Adding reverb with ReaVerbate to "brighten" or add depth to track
        4. Eliminate peaking/clipping using Kenny Goaia's split fade trick
        4. Add effects with envelopes (playrate, volume)
            1. Add FX to individual items (helmet effect)
    6. Can compare single tracks to joined tracks to show benefit of
       multiple phones
2. Beer recipes
3. Pocket amp with headphone jack
