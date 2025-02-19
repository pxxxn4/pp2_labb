import datetime

def five_days_ago():
    print(datetime.date.today() - datetime.timedelta(days=5))

def today_yest_tom():
    print(f"Today: {datetime.date.today()}\nYesterday: {datetime.date.today() - datetime.timedelta(days=1)}\nTomorrow: {datetime.date.today() + datetime.timedelta(days=1)}")

def del_microsec():
    def drop_ms(dt):
        return dt.replace(microsecond=0)

    now = datetime.datetime.now()
    print(f'Original: {now}')

    no_ms = drop_ms(now)
    print(f'Without microseconds: {no_ms}')

def sec_diff(d1_str, d2_str):
    fmt = '%Y-%m-%d'

    d1 = datetime.datetime.strptime(d1_str, fmt)
    d2 = datetime.datetime.strptime(d2_str, fmt)

    return (d2 - d1).total_seconds()

# d1 = '2024-02-17'
# d2 = '2024-02-18'

# print(f'Seconds difference: {sec_diff(d1, d2)}')
