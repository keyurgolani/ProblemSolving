import java.math.BigInteger
import java.sql.Timestamp
import java.util.*
import kotlin.collections.ArrayList

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

fun takeBigIntInput(): BigInteger {
    val input = Scanner(System.`in`)
    val value = input.nextBigInteger()
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

fun  getPisanoPeriod(number: Int): Int {
    val s = mutableListOf<Int>()
    var a: Int = 0
    var k: Int = 0
    var b: Int = 1
    while (s.subList(0, k).isNotEqualTo(s.subList(k, s.size)) || k == 0) {
        println(s)
        s.add(a % number)
        k = s.size / 2
        b += a
        a = b - a
    }
    return k
}

fun Int.toBigInteger(): BigInteger {
    return BigInteger.valueOf(this.toLong())
}

fun List<Int>.isEqualTo(other: List<Int>): Boolean {
    if (this.size != other.size) {
        return false
    }
    return (0..this.size - 1).all { this[it].equals(other[it]) }
}

fun List<Int>.isNotEqualTo(other: List<Int>): Boolean {
    if (this.size != other.size) {
        return true
    }
    return (0..this.size - 1).any { !this[it].equals(other[it]) }
}

fun timeit(closure: () -> Unit): Unit {
    val start = System.nanoTime()
    closure()
    println("\n\n-----------------------------------")
    println("Execution Time: ${((System.nanoTime() - start).toDouble() / 1000000000)} seconds")
    println("-----------------------------------\n\n")
}