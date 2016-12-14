from scraper.utils import is_valid_url


def test_is_valid_url_valid_urls():
    assert is_valid_url("") is False
    assert is_valid_url("http://") is False
    assert is_valid_url("htp://www.test.com") is False
    assert is_valid_url("http:/www.test.com") is False
    assert is_valid_url("www.test.com") is False


def test_is_valid_url_invalid_urls():
    assert is_valid_url("http://domain.com") is True
    assert is_valid_url("https://domain.com") is True
    assert is_valid_url("http://www.domain.com") is True
    assert is_valid_url("https://www.domain.com") is True
    assert is_valid_url("http://www.domain.co.uk") is True
    assert is_valid_url("https://www.domain.co.uk") is True


def test_is_redirect():
    assert False # TODO
