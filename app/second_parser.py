def parse_duration(sec: int) -> str:
    if sec == 0:
        raise ValueError ("Given value cannot be equal 0!")
    if sec < 0:
        raise ValueError ("Given value cannot be less than 0!")
    days = sec // 86400
    hours = (sec - days * 86400) // 3600
    minutes = (sec - days * 86400 - hours * 3600) // 60
    seconds = sec - days * 86400 - hours * 3600 - minutes * 60
    result = ("{}d ".format(days) if days else "") + \
    ("{}h ".format(hours) if hours else "") + \
    ("{}m ".format(minutes) if minutes else "") + \
    ("{}s ".format(seconds) [:-1] if seconds else "")
    return result