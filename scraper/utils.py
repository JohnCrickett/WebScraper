from urllib.parse import urlparse


def is_valid_url(url):
    """ Checks if the supplied URL appears to be valid
        returns True if it does, False otherwise
    """
    parse_results = urlparse(url)
    if parse_results.scheme and parse_results.netloc and \
       parse_results.scheme == 'http' or parse_results.scheme == 'https':
        return True
    return False


def is_redirect(response):
    """ Checks if the response is a redirect code, if so returns True
    """
    return response.status in (300, 301, 302, 303, 307)
