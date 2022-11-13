def parse_duration(sec: int) -> str:
    if sec < 0:
        raise ValueError ("Given value cannot be less than 0!")
    if sec == 0:
        return "0s"
    days = sec // 86400
    hours = (sec - days * 86400) // 3600
    minutes = (sec - days * 86400 - hours * 3600) // 60
    seconds = sec - days * 86400 - hours * 3600 - minutes * 60
    result= ("{}d ".format(int(days)) if days else "" ) + \
    ("{}h ".format(int(hours)) if hours else "" ) + \
    ("{}m ".format(int(minutes)) if minutes else "" ) + \
    ("{}s ".format(int(seconds)) if seconds else "")
    if result == days or hours or minutes or seconds or days and not hours or days and not minutes and days and not seconds or hours and not minutes or hours and not seconds or minutes and not seconds:
        return result [:-1]
    return result