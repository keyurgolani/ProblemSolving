'''

Intro - this is a short coding exercise with Python and Javascript.  We tried to make it as
platform and API version neutral as possible

Instructions:
  Task 1:  Already done as example.  It generates an ID value (kind of like a memory address)
           for a value difference of 1 between first list elements
           Checking others code is always encouraged however.

  Task 2:  Generate the prime numbers less then 100 (1 is not prime, but 2 is)
           Reverse each number (13 becomes 31)
           Perform a modulus 26 operation on each number (x%26)
           Add 97 to each number, comments about what this accomplishes are encouraged
           Convert each number into ascii, they should be in small letter range
           Combine into a string and return (hint, the last letter is 'b')

  Task 3:  Update file foo.txt file with your name, the task 1 id value, and
           the task 2 string.
           Either editing the file in place or over-writing with new version is fine

  Task 4:  Load the html file into your favorite browser, verify that the Alert works.
           Convert Alert to the min version of the SweetAlert2 api.  Google for download
           and examples.

Notes:
  1.  Google and Stack Overflow are your friends
  2.  http://learnxinyminutes.com is a great site if python or javascript is new to you
  3.  Bonus points for short functions where the name starts with verb
  4.  Even more bonus points for keeping code so short that functions aren't needed.
  5.  Don't stress, we believe in partial credit
  6.  Some comments are great, but don't go too overboard
  7.  We took this approach because we hate coding on a white board for interviews ourselves,
      but understand it's an inconvenience.  Thanks for your time
'''

from __future__ import print_function


def diff_one_id(a, b):
    return id(b[0] - a[0])


def task_1():
    a = [10]
    b = a
    b[0] += 1
    return diff_one_id(a, b)


def task_2():
    return ''.join([chr(((divmod(num, 10)[1] * 10 + divmod(num, 10)[0]) % 26) + 97)
                    for num in range(2, 100) if all([num % i != 0 for i in range(2, num)])])


def task_3():
    # Read in the file
    with open('foo.txt', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('placeholder1', 'Keyur').replace(
        'placeholder2', str(task_1())).replace('placeholder3', task_2())

    # Write the file out again
    with open('foo.txt', 'w') as file:
        file.write(filedata)


def main():
    result_1 = task_1()
    print(task_2())
    task_3()
    print("result 1: ", result_1)


if __name__ == '__main__':
    main()


""" PUT BELOW IN FILE foo.txt

let text = `
I am placeholder1\n my id value is placeholder2\n my string is placeholder 3
`;

"""

""" PUT BELOW IN FILE your-name.html

<!DOCTYPE html>
<html>
   <head> <title>demo</title>
       <script type="text/javascript">
                function doSomething() {
                         alert(text)
                }
        </script>
   </head>
   <body>
        <script src="foo.txt"></script>

        <center>
        <input type="button"
                value="Click if you like AiNuco"
                onclick="doSomething()"
                style="width: 600px;
                height: 200px;
                border: 10px solid blue;
                color:red;
                background-color:pink;
                font-size: 50px;"
                >
        </center>
   </body>
</html>

"""
