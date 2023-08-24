from datetime import datetime


def remove_spaces(string_with_spaces: str) -> str:
    """
    Removes spaces from a string and returns it.

    Args:
        string_with_spaces : str
            String you want to remove spaces from.

    Returns:
        string_without_spaces : str
            String with spaces removed.
    """

    string_without_spaces: str = "".join(string_with_spaces.split())
    return string_without_spaces


def to_upper(lowercase_string: str) -> str:
    """
    Capitalizes every letter in `lowercase_string`.

    Args:
        lowercase_string : str
            String with lowercase letters.

    Returns:
        uppercase_string : str
            String with no lowercase letters.
    """

    uppercase_string: str = lowercase_string.upper()
    return uppercase_string


def format_datetime(datetime: datetime) -> str:
    """
    Formats the datetime object into a string
    accepted by the Airfrance-KLM API.

    Args:
        datetime : datetime
            Datetime object you want formatted

    Returns:
        formatted_datetime : str
            Datetime object formatted as a string.
    """

    formatted_datetime: str = datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    return formatted_datetime
