import java.math.BigInteger

/**
 * Created by keyurgolani on 6/1/17.
 */

fun sumNumbers(values:List<Int>): Int {
    var answer: Int = 0
    for (value in values) {
        answer += value
    }
    return answer
}

fun  maxPairwiseProduct(values: List<Int>): Int {
    var maxOne = Int.MIN_VALUE
    var maxTwo = Int.MIN_VALUE
    var minOne = Int.MAX_VALUE
    var minTwo = Int.MAX_VALUE
    for (value in values) {
        if (value >= maxOne) {
            maxTwo = maxOne
            maxOne = value
        } else if (value >= maxTwo) {
            maxTwo = value
        }
        if (value <= minOne) {
            minTwo = minOne
            minOne = value
        } else if (value <= minTwo) {
            minTwo = value
        }
    }
    val maxProduct = maxOne * maxTwo
    val minProduct = minOne * minTwo
    return if (minProduct > maxProduct) minProduct else maxProduct
}

fun  maxPairwiseSum(values: List<Int>): Int {
    var maxOne = Int.MIN_VALUE
    var maxTwo = Int.MIN_VALUE
    for (value in values) {
        if (value >= maxOne) {
            maxTwo = maxOne
            maxOne = value
        } else if (value >= maxTwo) {
            maxTwo = value
        }
    }
    return maxOne + maxTwo
}

fun  fibonacciSeriesTill(position: Int): List<BigInteger> {
    val fibonacci: MutableList<BigInteger> = mutableListOf(BigInteger.ZERO, BigInteger.ONE)
    if (position > 1) {
        (2..position - 1).forEach { fibonacci.add(it, fibonacci[it - 1] + fibonacci[it - 2]) }
    }
    return fibonacci
}

fun  fibonacciNumberAt(position: Int): BigInteger {
    val fibonacci: MutableList<BigInteger> = mutableListOf(BigInteger.ZERO, BigInteger.ONE)
    if (position > 1) {
        (2..position - 1).forEach {
            fibonacci[1] = fibonacci[0] + fibonacci[1]
            fibonacci[0] = fibonacci[1] - fibonacci[0]
        }
    }
    return fibonacci[1]
}

fun  lastDigitOfFibonacciNumberAt(position: Int): Int {
    val fibonacci: MutableList<Int> = mutableListOf(0, 1)
    if (position > 1) {
        (2..position - 1).forEach {
            fibonacci[1] = fibonacci[0] % 10 + fibonacci[1] % 10
            fibonacci[0] = fibonacci[1] % 10 - fibonacci[0] % 10
        }
    }
    return (((fibonacci[1] % 10) + 10) % 10)
}

fun  gcdOf(number1: BigInteger, number2: BigInteger): BigInteger {
    var num1 = number1
    var num2 = number2
    while (num2 != BigInteger.ZERO) {
        val temp = num2
        num2 = num1 % num2
        num1 = temp
    }
    return num1
}