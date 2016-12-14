import argparse
import logging

from scraper import run_scraper
from scraper.utils import is_valid_url


def main():
    parser = argparse.ArgumentParser(description='Crawl a website.')
    parser.add_argument("-u",
                        "--url",
                        help='the root URL of the website to crawl')
    parser.add_argument("-ll",
                        "--loglevel",
                        default=0,
                        help='the log level to use')

    args = parser.parse_args()
    levels = [logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]
    logging.basicConfig(level=levels[min(int(args.loglevel), len(levels) - 1)])
    url = args.url
    if is_valid_url(url):
        print('Scraping website: {url}'.format(url=url))
        run_scraper(url)
    else:
        print('Error, URL does not appear to be valid, '
              'please check and try again')


if __name__ == '__main__':
    main()
