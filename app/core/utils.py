import hashlib

def millis_converter(milli: int) -> str:
    """
    Converts milliseconds to MM:SS format.
    """
    total_seconds = milli / 1000
    minutes, seconds = divmod(total_seconds, 60)
    seconds_formatted = f"{seconds:02.0f}"
    return f"{round(minutes)}:{seconds_formatted}"

def hash_string(url: str | None) -> str:
    if isinstance(url, str):
        hash_object = hashlib.sha256()
        hash_object.update(url.encode('utf-8'))
        return hash_object.hexdigest()
    return None