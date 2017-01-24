import calendar
date = tuple(map(int, raw_input().split()))
print(['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'][calendar.weekday(date[2], date[0], date[1])])
