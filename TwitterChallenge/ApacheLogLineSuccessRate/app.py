import sys
import re

logParseRegex = '([1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]) ([^\s]*) ([^\s]*) (\[.*\]) (\".*?\") (\d{3}) (\d*) (\d*) (\".*?\") ([1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9])'
months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

def solution(lines):
    urls = {}
    for line in lines:
        values = re.match(logParseRegex, line).groups()
        day, hour, minute, _ = values[3].strip("[]").split(':')
        date, month, year = day.split("/")
        url = values[4].split(" ")[1].split("?")[0]
        status = int(values[5])
        formattedDate = "{}-{}-{}T{}:{}".format(year, months[month], date, hour, minute)
        try:
            if 600 > status >= 500:
                urls[formattedDate, url][0] += 1
                urls[formattedDate, url][1] += 1
            else:
                urls[formattedDate, url][1] += 1
        except KeyError:
            if 600 > status >= 500:
                urls[formattedDate, url] = [1, 1]
            else:
                urls[formattedDate, url] = [0, 1]
    return urls


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    for url, statuses in sorted(solution(lines).items(), key=lambda x: x[0]):
        print "%s %s %.2f" % (url[0], url[1], 100 - (float(statuses[0]) / float(statuses[1])) * 100)


if __name__ == '__main__':
    main()
