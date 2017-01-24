import re
for _ in range(int(input())):
    try:
        reg_str = re.compile(raw_input())
    except:
        print False
    else:
        print True
