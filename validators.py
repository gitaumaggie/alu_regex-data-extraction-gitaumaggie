
import re

# 1. Email address
EMAIL_PATTERN = (
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+"
    r"(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
)

# 2. URLs
URL_PATTERN = (
    r"^https?://(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}"
    r"(?::\d{1,5})?(?:/[^\s]*)?$"
)

# 3. Phone numbers
PHONE_PATTERN = (
    r"^(?:"
    r"\(\d{3}\) \d{3}-\d{4}"
    r"|\d{3}-\d{3}-\d{4}"
    r"|\d{3}\.\d{3}\.\d{4}"
    r")$"
)

# 4. Credit card numbers
CREDIT_CARD_PATTERN = (
    r"^\d{4}([ -])\d{4}\1\d{4}\1\d{4}$"
)

# 5. Time (12-hour and 24-hour formats)
TIME_PATTERN = (
    r"^(?:"
    r"(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)"
    r"|"
    r"(?:[01]\d|2[0-3]):[0-5]\d"
    r")$"
)

# 6. HTML tags
HTML_TAG_PATTERN = (
    r"^<[A-Za-z][A-Za-z0-9]*"
    r"(?:\s+[^<>]*)?/?\s*>$"
)

# 7. Hashtags
HASHTAG_PATTERN = r"^#[A-Za-z0-9_]+$"

# 8. Currency amounts
CURRENCY_PATTERN = (
    r"^\$(?:\d+|[1-9]\d{0,2}(?:,\d{3})+)\.\d{2}$"
)


def validate_email(value):
    return bool(re.fullmatch(EMAIL_PATTERN, value))


def validate_url(value):
    return bool(re.fullmatch(URL_PATTERN, value))


def validate_phone(value):
    return bool(re.fullmatch(PHONE_PATTERN, value))


def validate_credit_card(value):
    return bool(re.fullmatch(CREDIT_CARD_PATTERN, value))


def validate_time(value):
    return bool(re.fullmatch(TIME_PATTERN, value, re.IGNORECASE))


def validate_html_tag(value):
    return bool(re.fullmatch(HTML_TAG_PATTERN, value))


def validate_hashtag(value):
    return bool(re.fullmatch(HASHTAG_PATTERN, value))


def validate_currency(value):
    return bool(re.fullmatch(CURRENCY_PATTERN, value))
