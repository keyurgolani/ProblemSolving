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
    7. GCD of Two Numbers
    """)
    var closure = {  }
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
            closure = {
                println("Maximum Pairwise Product")
                val input: List<Int> = takeArrayIntInput()
                timeit { println(maxPairwiseProduct(input)) }
            }
        }
        3 -> {
            closure = {
                println("Maximum Pairwise Sum")
                val input: List<Int> = takeArrayIntInput()
                timeit { println(maxPairwiseSum(input)) }
            }
        }
        4 -> {
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
            closure = {
                val position: Int = takeIntInput()
                println("Fibonacci Number at Position $position")
                timeit { println(fibonacciNumberAt(position)) }
            }
        }
        6 -> {
            closure = {
                val position: Int = takeIntInput()
                println("Last Digit of Fibonacci Number at Position $position")
                timeit { println(lastDigitOfFibonacciNumberAt(position)) }
            }
        }
        7 -> {
            closure = {
                val (number1, number2) = takeTwoBigIntInput()
                println("GCD of $number1 and $number2")
                timeit { println(gcdOf(number1, number2)) }
            }
        }
        8 -> {
            closure = {

            }
        }
        else -> {
            closure = {

            }
        }
    }

    // Executing
    closure()

}
