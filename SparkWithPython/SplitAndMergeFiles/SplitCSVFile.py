import sys
import csv
import os


def split_csv(filepath, delimiter=',', row_limit=100,
          output_name_template='output_{}.csv', output_path='.', keep_headers=True):
    reader = csv.reader(open(filepath, 'r'), delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template.format(current_piece)
    )
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.next()
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template.format(current_piece)
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)


def main():
    split_csv(sys.argv[1], row_limit=int(sys.argv[2]));


main()
