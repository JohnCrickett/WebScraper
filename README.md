# WebScraper
Python Web Scraper

To setup the environment create a new virtual environment for Python 3.5 using
either virtualenv or Anaconda then activate the environment.
 
Then checkout this git repo and run either:

`make pipinit`

or

`make condainit
`
as appropriate for your choice of virtual environment. This will install the 
required libraries.

To verify all is well you can then run the unit test suite using:

`make test`

if all pass then the scraper and environment are installed and setup correctly.

You can then run the scraper using:

`python scraper -u <URL>`

Where you replace <URL> with the URL of the site you wish to scrape.
