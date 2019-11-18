def interval_to_seconds(interval):
    if 'second' in interval:
        multiplier = 1
    elif 'minute' in interval:
        multiplier = 60
    elif 'hour' in interval:
        multiplier = 3600
    elif 'day' in interval:
        multiplier = 86400
    else:
        return 0

    _time = interval.strip().split('(')[1]
    _number = _time.strip().split(' ')[0]
    print(int(_number) * multiplier)
    return int(_number) * multiplier

assert interval_to_seconds('rate(5 minutes)') == 300
assert interval_to_seconds('     rate(5 minutes)') == 300
assert interval_to_seconds('   rate(     5 minutes)') == 300
assert interval_to_seconds('   rate(     5       minutes       )') == 300
assert interval_to_seconds('   rate     (     5       minutes       )') == 300

assert interval_to_seconds('rate(1 minute)') == 60
assert interval_to_seconds('cron(....)') == 0
