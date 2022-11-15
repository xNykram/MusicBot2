def parse_duration(sec: int) -> str:
    if sec < 0:
        raise ValueError("Given value cannot be less than 0!")
    if sec == 0:
        return "0s"
    days = sec // 86400
    hours = (sec - days * 86400) // 3600
    minutes = (sec - days * 86400 - hours * 3600) // 60
    seconds = sec - days * 86400 - hours * 3600 - minutes * 60
    result = (
        (f"{int(days)}d " if days else "")
        + (f"{int(hours)}h " if hours else "")
        + (f"{int(minutes)}m " if minutes else "")
        + (f"{int(seconds)}s " if seconds else "")
    )

    return result.rstrip()
