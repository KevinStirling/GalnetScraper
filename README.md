# GalnetScraper
Super simple scraper for Galnet news articles, converted to json

The intention of this scraper is to generate a json output suitable for importing to a DGraph database, which will be used for the TinFoilGalnet project.


Currently, the scraper is only set to grab all the articles between years 3301 and 3305 via hardcoding. Considering making it dynamic in the future, but I'm really only running this once for my use case, so it's not really a priority.


# How to use it yourself

1. Set up a python3 virtual environment in the directory where you cloned the repo:

`$ python3 -m venv venv`

`$ . ./venv/bin/activate`

2. Install required dependancies

Depending on how you configured your pip installation:

`$ pip install requests BeautifulSoup4`

or

`$ pip3 install requests BeautifulSoup4`

3. Run it

`$ python3` 

`>>> from main import main`

`>>> main()`
