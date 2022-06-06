from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_counter():
    actual = get_citations_needed_count()
    expected = 5
    assert actual == expected


def test_report():
    actual = get_citations_needed_report()[0:38]
    expected = """The following paragraphs need citation"""
    assert actual == expected
