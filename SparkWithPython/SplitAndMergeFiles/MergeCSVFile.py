import sys
import os

def mergeFile(output_file_name, file_count, delimiter=',',
          input_path='.', input_name_template='input_{}.csv', output_path='.', merge_headers=True):
    fout = open(os.path.join(
        output_path,
        output_file_name
    ), 'a')

    # now the rest:
    for num in range(1,file_count + 1):
        f = open(os.path.join(
            input_path,
            input_name_template.format(str(num))
        ))
        if merge_headers:
            first_line = True
        else:
            first_line = False
        for line in f:
            if not first_line or num == 1:
                fout.write(line)
                first_line = False
            first_line = False
        f.close() # not really needed
    fout.close()


def main():
    mergeFile(sys.argv[1], int(sys.argv[2]), input_path=sys.argv[3], input_name_template = sys.argv[4] + '{}.csv')


main()
