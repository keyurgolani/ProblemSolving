/**
 * Created by keyurgolani on 6/3/17.
 */

fun main(args: Array<String>) {
    while (true) {
        val value: Int = (Math.random() * 100).toInt()
        if(lastDigitOfFibonacciNumberAt(value) < 0) {
            println(value)
            break
        } else {
            println("OK")
        }
    }
}