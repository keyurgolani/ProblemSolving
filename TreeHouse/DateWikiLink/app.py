import datetime

link = 'https://en.wikipedia.org/wiki/{}'
link_format = '%b_%d'
input_format = '%m/%d'

while True:
    answer = raw_input("What date would you like to lookup? Please use MM/DD format. Enter 'quit' to quit\n>")
    if answer.upper() == 'QUIT':
        break

    try:
        date = datetime.datetime.strptime(answer, input_format)
        print link.format(date.strftime(link_format))
    except ValueError:
        print 'That is not a date with a valid format! Please try again!'
