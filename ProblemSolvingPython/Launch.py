import Module1 as MOne
import Utilities as Util


def main():
    choice = input("""Enter Operation:
    
    1. Sum Of Inputs
    2. Maximum Pairwise Product
    3. Maximum Pairwise Sum
    4. Fibonacci Series Till Number
    5. Fibonacci Number at position
    6. Last Digit of Fibonacci Number at position
    7. Fibonacci Number at position modulo given number
    8. Last digit of sum of fibonacci numbers till position
    9. Last digit of partial sum of fibonacci numbers from start till limit
    10. GCD of Two Numbers
    11. LCM of Two Numbers
    
""")

    if choice == 1:
        # Sum of input numbers
        def closure():
            print "Sum of Numbers"
            print MOne.sum_of_numbers(Util.take_int_array_input())
    elif choice == 2:
        # Maximum Pairwise Product
        def closure():
            print "Maximum Pairwise Product"
            print MOne.max_pairwise_product(Util.take_int_array_input())
    elif choice == 3:
        # Maximum Pairwise Sum
        def closure():
            print "Maximum Pairwise Sum"
            print MOne.max_pairwise_sum(Util.take_int_array_input())
    elif choice == 4:
        # Fibonacci Series till number
        def closure():
            limit = Util.take_int_input(1)
            print "Fibonacci Series till {}".format(*limit)
            for fibonacci_number in MOne.fibonacci_series(*limit):
                print fibonacci_number,
    elif choice == 5:
        # Fibonacci Number at position
        def closure():
            position = Util.take_int_input(1)
            print "Fibonacci Number at {}".format(*position)
            print MOne.fibonacci_number(*position)
    elif choice == 6:
        # Last Digit of Fibonacci Number at position
        def closure():
            position = Util.take_int_input(1)
            print "Last Digit of Fibonacci Number at {}".format(*position)
            print MOne.fibonacci_number_last_digit(*position)
    elif choice == 7:
        # Fibonacci Number at position modulo given number
        def closure():
            values = Util.take_int_input(2)
            print "Fibonacci Number at {} modulo {}".format(*values)
            print MOne.fibonacci_number_modulo(*values)
    elif choice == 8:
        # Last digit of sum of fibonacci numbers till limit
        def closure():
            limit = Util.take_int_input(1)
            print "Last digit of sum of fibonacci numbers till position {}".format(*limit)
            print MOne.last_digit_of_sum_of_fibonacci_numbers_till(*limit)
    elif choice == 9:
        # Last digit of partial sum of fibonacci numbers from start till limit
        def closure():
            bounds = Util.take_int_input(2)
            print "Last digit of partial sum of fibonacci numbers from {} till {}".format(*bounds)
            print MOne.last_digit_of_partial_sum_of_fibonacci_numbers(*bounds)
    elif choice == 10:
        # GCD of two numbers
        def closure():
            numbers = Util.take_int_input(2)
            print "GCD of {} and {}".format(*numbers)
            print MOne.gcd(*numbers)
    elif choice == 11:
        # LCM of two numbers
        def closure():
            numbers = Util.take_int_input(2)
            print "LCM of {} and {}".format(*numbers)
            print MOne.lcm(*numbers)
    else:
        # Default Case
        def closure():
            print "Option Not Implemented Yet!\nExiting."
            pass

    # Executing
    Util.timeit(closure=closure)


if __name__ == '__main__':
    main()
