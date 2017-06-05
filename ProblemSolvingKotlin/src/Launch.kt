/**
 * Created by keyurgolani on 6/1/17.
 */

fun main(args: Array<String>) {
    println("""Enter Operation:

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
    var closure: () -> Unit
    when(takeIntInput()) {
        1 -> {
            // Sum of all inputs
            closure = {
                println("Sum of Inputs")
                val input: List<Int> = takeArrayIntInput()
                timeit { println(sumNumbers(input)) }
            }
        }
        2 -> {
            // Maximum Pairwise Product
            closure = {
                println("Maximum Pairwise Product")
                val input: List<Int> = takeArrayIntInput()
                timeit { println(maxPairwiseProduct(input)) }
            }
        }
        3 -> {
            // Maximum Pairwise Sum
            closure = {
                println("Maximum Pairwise Sum")
                val input: List<Int> = takeArrayIntInput()
                timeit { println(maxPairwiseSum(input)) }
            }
        }
        4 -> {
            // Fibonacci Series till number
            closure = {
                val position: Int = takeIntInput()
                println("Fibonacci Series Till Position $position")
                timeit {
                    for (fibonacciNumber in fibonacciSeriesTill(position)) {
                        print("$fibonacciNumber ")
                    }
                }
            }
        }
        5 -> {
            // Fibonacci Number at position
            closure = {
                val position: Int = takeIntInput()
                println("Fibonacci Number at Position $position")
                timeit { println(fibonacciNumberAt(position)) }
            }
        }
        6 -> {
            // Last Digit of Fibonacci Number at position
            closure = {
                val position: Int = takeIntInput()
                println("Last Digit of Fibonacci Number at Position $position")
                timeit { println(lastDigitOfFibonacciNumberAt(position)) }
            }
        }
        7 -> {
            // Fibonacci Number at position modulo given number
            closure = {
                val (position, number) = takeTwoBigIntInput()
                println("Fibonacci Number at Position $position modulo $number")
                timeit { println(fibonacciNumberAtModulo(position, number.toInt())) }
            }
        }
        8 -> {
            // Last digit of sum of fibonacci numbers till limit
            closure = {
                val position: Int = takeIntInput()
                println("Last Digit of Sum of Fibonacci Numbers till Position $position")
                timeit { println(lastDigitOfSumOfFibonacciNumbersTill(position)) }
            }
        }
        9 -> {
            // Last digit of partial sum of fibonacci numbers from start till limit
            closure = {
                val (start, end) = takeTwoIntInput()
                println("Last Digit of Partial Sum of Fibonacci Numbers from Position $start till Position $end")
                timeit { println(lastDigitOfPartialSumOfFibonacciNumbers(start, end)) }
            }
        }
        10 -> {
            // GCD of two numbers
            closure = {
                val (number1, number2) = takeTwoBigIntInput()
                println("GCD of $number1 and $number2")
                timeit { println(gcdOf(number1, number2)) }
            }
        }
        11 -> {
            // LCM of two numbers
            closure = {
                val (number1, number2) = takeTwoBigIntInput()
                println("LCM of $number1 and $number2")
                timeit { println(lcmOf(number1, number2)) }
            }
        }
        else -> {
            // Default Case
            closure = {
                println("Option Not Implemented Yet!\nExiting.")
            }
        }
    }

    // Executing
    closure()

}
