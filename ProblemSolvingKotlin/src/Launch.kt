/**
 * Created by keyurgolani on 6/1/17.
 */

fun main(args: Array<String>) {
    println("""Enter Operation:

    1. Sum Of Inputs
    2. Maximum Pairwise Product
    3. Maximum Pairwise Sum
    4. Fibonacci Series Till Number
    4. Fibonacci Number
    5. Fibonacci Number at position
    6. Last Digit of Fibonacci Number at position
    7. GCD of Two Numbers
    """)
    var closure = {  }
    when(takeIntInput()) {
        1 -> {
            closure = {
                println("Sum of Inputs")
                val input: List<Int> = takeArrayIntInput()
                timeit { println(sumNumbers(input)) }
            }
        }
        2 -> {
            closure = {

            }
        }
        3 -> {
            closure = {

            }
        }
        4 -> {
            closure = {

            }
        }
        5 -> {
            closure = {

            }
        }
        6 -> {
            closure = {

            }
        }
        7 -> {
            closure = {

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