import pytest
from page_generator import extract_title


def test_extract_title_basic():
    assert extract_title("# Hello") == "Hello"


def test_extract_title_with_spaces():
    assert extract_title("#   World   ") == "World"


def test_extract_title_no_h1_raises():
    with pytest.raises(Exception):
        extract_title("## No H1 here")
