To Do:
- Decide on navbar background color
    - Notebook page looks jarring with white background
    - Individual articles look better with white background

Steps for setting up Pelican Blog:
- Install Python (Anaconda/Miniconda distribution)
  - https://docs.conda.io/en/latest/miniconda.html
- Create new conda env (pelican)
  - `conda create --name pelican python` (creates "empty" conda distribution with just python)
- Install Git
  - On Ubuntu as easy as:
    - `sudo apt-get update`
    - `sudo apt install git`

To build local site:
```
pelican -s pelicanconf.py
```

To launch devserver at localhost:8000:
```
pelican --listen
```

**NOTE:** BEWARE OF BROWSER CACHING, when using localhost (CSS file)

To build site for Github Pages:
```
pelican -s publishconf.py
```
