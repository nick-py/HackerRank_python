def timeConversion(s):
    period = s[8:10]
    time = s[0:8].split(':')
    if period == "PM":
        hour = (int(time[0]) + 12) if time[0] != "12" else "12"
    else:
        hour = time[0] if time[0] != "12" else "00"

    return "{}:{}:{}".format(hour, time[1], time[2])


s = input().strip()
result = timeConversion(s)
print(result)
print(result)