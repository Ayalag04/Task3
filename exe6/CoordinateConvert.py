def dd_to_dms(dd, is_lat=True):
    deg = int(abs(dd))
    min_float = (abs(dd) - deg) * 60
    min_ = int(min_float)
    sec = round((min_float - min_) * 60, 2)  # עיגול ל-2 ספרות אחרי הנקודה
    if is_lat:
        direction = 'N' if dd >= 0 else 'S'
    else:
        direction = 'E' if dd >= 0 else 'W'
    return [deg, min_, sec, direction]

coordinates = {
    "anchorage": [-149.9002, 61.2181, 22],
    "los_angeles": [-118.2437, 34.0522]
}

converted = {}
for city, vals in coordinates.items():
    converted[city] = [
        dd_to_dms(vals[0], is_lat=False),
        dd_to_dms(vals[1], is_lat=True)
    ]
    if len(vals) > 2:  # אם יש ערך נוסף (כמו 22 ב-Anchorage)
        converted[city].append(vals[2])

print(converted)
