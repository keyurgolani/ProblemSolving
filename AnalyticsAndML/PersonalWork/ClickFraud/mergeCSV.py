import csv


def mergeCSV(fileList):
    writer = open("merged.csv", 'a')
    reader1 = csv.reader(open(fileList[0]))
    for line in reader1:
        writer.write(line)
    for file in fileList[1:]:
        reader = csv.reader(open(file))
        for line in reader[1:]:
            writer.write(line)


def main():
    mergeCSV(['Results1.csv', 'Results2.csv'])


if __name__ == '__main__':
    main()
