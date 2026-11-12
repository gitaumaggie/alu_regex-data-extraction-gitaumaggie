import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validators import (
    validate_email,
    validate_url,
    validate_phone,
    validate_credit_card,
    validate_time,
    validate_html_tag,
    validate_hashtag,
    validate_currency
)


def test_email():
    assert validate_email("user@example.com") is True
    assert validate_email("invalid-email") is False


def test_url():
    assert validate_url("https://www.example.com") is True
    assert validate_url("https://subdomain.example.org/page") is True
    assert validate_url("example.com") is False


def test_phone():
    assert validate_phone("(123) 456-7890") is True
    assert validate_phone("123-456-7890") is True
    assert validate_phone("123.456.7890") is True
    assert validate_phone("1234567890") is False


def test_credit_card():
    assert validate_credit_card("1234 5678 9012 3456") is True
    assert validate_credit_card("1234-5678-9012-3456") is True
    assert validate_credit_card("1234-5678 9012-3456") is False


def test_time():
    assert validate_time("14:30") is True
    assert validate_time("2:30 PM") is True
    assert validate_time("25:90") is False


def test_html_tag():
    assert validate_html_tag("<p>") is True
    assert validate_html_tag('<div class="example">') is True
    assert validate_html_tag(
        '<img src="image.jpg" alt="description">'
    ) is True


def test_hashtag():
    assert validate_hashtag("#example") is True
    assert validate_hashtag("#ThisIsAHashtag") is True
    assert validate_hashtag("example") is False


def test_currency():
    assert validate_currency("$19.99") is True
    assert validate_currency("$1,234.56") is True
    assert validate_currency("$19.9") is False