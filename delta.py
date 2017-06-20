def get_years_diff(first_year, last_year):
    if first_year == last_year:
        return 0
    else:
        return (abs(first_year - last_year) - 1) * 365


def get_months_diff(first_month, last_month):
    months = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30,
              'Oct': 31, 'Nov': 30, 'Dec': 31}
    """for year in years:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Para años bisiestos
            months['Feb'] = 29"""
    return abs(months[first_month] - months[last_month])


def get_days_diff(first_day, last_day):
    return abs(int(first_day) - int(last_day))


def get_hours_diff(first_hour, last_hour):
    hour_1 = first_hour.split(":")
    hour_2 = last_hour.split(":")
    return abs(int(hour_1[0]) - int(hour_2[0])) + abs((int(hour_1[1]) - int(hour_2[1])) / 60) \
           + abs((int(hour_1[2]) - int(hour_2[2])) / 3600)


def get_time_zone_diff(first_time, last_time):
    if first_time[0] != last_time[0]:
        return abs(int(first_time[1]) + int(last_time[1])) * 10 + abs(int(first_time[2]) + int(last_time[2])) \
           + abs(int(first_time[3:]) + int(last_time[3:])) / 60
    else:
        return abs(int(first_time[1]) - int(last_time[1])) * 10 + abs(int(first_time[2]) - int(last_time[2])) \
           + abs(int(first_time[3:]) - int(last_time[3:])) / 60


def get_total_diff(first_ts, last_ts):
    date_1 = first_ts.split(" ")
    date_2 = last_ts.split(" ")
    days = get_days_diff(date_1[1], date_2[1])
    months = get_months_diff(date_1[2], date_2[2])
    years = get_years_diff(date_1[3], date_2[3])
    hours = get_hours_diff(date_1[4], date_2[4])
    total_days = days + months + years
    time_z = get_time_zone_diff(date_1[5], date_2[5])
    total_hours = (total_days * 24) + hours - time_z
    return abs(int(total_hours * 3600))


def main():
    results = []
    cases = int(input())
    while cases != 0:
        ts_1 = input()
        ts_2 = input()
        results.append(get_total_diff(ts_1, ts_2))
        cases -= 1

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
