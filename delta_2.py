from datetime import datetime


def main():
    results = []
    date_format = "%a %d %b %Y %H:%M:%S %z"
    for _ in range(int(input())):
        date_1 = datetime.strptime(input(), date_format)
        date_2 = datetime.strptime(input(), date_format)
        results.append(abs(int((date_1-date_2).total_seconds())))

    for result in results:
        print(result)


if __name__ == '__main__':
    main()