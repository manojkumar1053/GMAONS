def days_needed(kellyDaily, samDaily, difference):
    x = difference / (kellyDaily - samDaily)
    if x <= 0: return -1
    return int(x+1)
