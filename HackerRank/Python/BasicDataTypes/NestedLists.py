marks = {}
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    try :
        marks[score]
    except:
        marks[score] = [name]
    else:
        marks[score].append(name)
marks_list = marks.keys()
marks_list.sort()
lowest = marks_list[0]
while True:
    try:
        marks_list.remove(lowest)
    except ValueError:
        break
for name in sorted(marks[marks_list[0]]):
    print name
