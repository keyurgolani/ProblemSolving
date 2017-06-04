import java.math.BigInteger
import java.sql.Timestamp
import java.util.*

/**
 * Created by keyurgolani on 6/3/17.
 */

// Utility Functions

val takeArrayIntInput = {readLine()!!.split(" ").map { it.toInt() }}


fun takeIntInput(): Int {
    // Assuming user will always enter something for input
    val input = Scanner(System.`in`)
    val value = input.nextInt()
    return value
}

fun takeTwoIntInput(): Pair<Int, Int> {
    // Assuming user will always enter something for input
    val input = Scanner(System.`in`)
    val value1 = input.nextInt()
    val value2 = input.nextInt()
    return Pair(value1, value2)
}

fun takeTwoBigIntInput(): Pair<BigInteger, BigInteger> {
    // Assuming user will always enter something for input
    val input = Scanner(System.`in`)
    val value1: BigInteger = input.nextBigInteger()
    val value2: BigInteger = input.nextBigInteger()
    return Pair(value1, value2)
}

fun timeit(closure: () -> Unit): Unit {
    val start = System.nanoTime()
    closure()
    println("\n\n-----------------------------------")
    println("Execution Time: ${((System.nanoTime() - start).toDouble() / 1000000000)} seconds")
    println("-----------------------------------\n\n")
}