# Hydrogen

A lightweight, minimalist theme for Pelican. Built from scratch. No bootstrap. No jQuery. Perfect for a personal website or blog.

I am not a web-developer. If you are and you can make this theme better,
then feel free to fork or contribute!

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

TO DO:
- Need to create conda env or pip requirements.txt with dependencies.
- Fix footer URLs. Direct all to github. More permanent?
