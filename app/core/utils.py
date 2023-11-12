def millis_converter(milli: int) -> str:
    """
    Converts milliseconds to MM:SS format.
    """
    total_seconds = milli / 1000
    minutes, seconds = divmod(total_seconds, 60)
    seconds_formatted = f"{seconds:02.0f}"
    return f"{round(minutes)}:{seconds_formatted}"
