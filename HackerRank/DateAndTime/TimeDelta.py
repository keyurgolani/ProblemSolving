# NOTE: Please use Python 3.x for this. Python 2.x does not support %z option for datetime.strptime

from datetime import datetime

for i in range(int(input())):
    print(int(abs((datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z') -
                   datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')).total_seconds())))
