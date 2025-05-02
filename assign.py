def format_text(text: str, prefix: str = "", suffix: str = "", capitalize: bool = False, max_length: int = None) -> str:
    """
    Formats the input text with optional prefix, suffix, capitalization, and max length.

    Parameters:
    - text (str): The input text to format.
    - prefix (str): A prefix to add. Default is "".
    - suffix (str): A suffix to add. Default is "".
    - capitalize (bool): Capitalize the text. Default is False.
    - max_length (int or None): Truncate the text to this length if provided.

    Returns:
    - str: Formatted text.

    Raises:
    - TypeError: If the input types are incorrect.

    Example:
    >>> format_text("hello", prefix="[", suffix="]", capitalize=True)
    '[Hello]'
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(max_length, (int, type(None))):
        raise TypeError("max_length must be an integer or None.")

    if capitalize:
        text = text.capitalize()

    result = f"{prefix}{text}{suffix}"

    if max_length is not None:
        result = result[:max_length]

    return result
#call function
print(format_text("hello", prefix="[", suffix="]", capitalize=True))
