import datetime


def counting_sundays(first_year, last_year):
    sunday_count = 0
    for year in range(first_year, last_year + 1):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                sunday_count += 1

    return sunday_count


print(counting_sundays(1901, 2000))  # 171
