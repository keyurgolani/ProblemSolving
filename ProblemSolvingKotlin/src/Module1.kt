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

fun maxPairwiseProduct(values: List<Int>): Int {
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

fun maxPairwiseSum(values: List<Int>): Int {
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

fun fibonacciSeriesTill(position: Int): List<BigInteger> {
    val fibonacci: MutableList<BigInteger> = mutableListOf(BigInteger.ZERO, BigInteger.ONE)
    if (position > 1) {
        (2..position - 1).forEach { fibonacci.add(it, fibonacci[it - 1] + fibonacci[it - 2]) }
    }
    return fibonacci
}

fun fibonacciNumberAt(position: Int): BigInteger {
    val fibonacci: MutableList<BigInteger> = mutableListOf(BigInteger.ZERO, BigInteger.ONE)
    if (position > 1) {
        (2..position).forEach {
            fibonacci[1] = fibonacci[0] + fibonacci[1]
            fibonacci[0] = fibonacci[1] - fibonacci[0]
        }
    }
    return fibonacci[1]
}

fun lastDigitOfFibonacciNumberAt(position: Int): Int {
    val fibonacci: MutableList<Int> = mutableListOf(0, 1)
    if (position > 1) {
        (2..position - 1).forEach {
            fibonacci[1] = fibonacci[0] % 10 + fibonacci[1] % 10
            fibonacci[0] = fibonacci[1] % 10 - fibonacci[0] % 10
        }
    }
    return (((fibonacci[1] % 10) + 10) % 10)
}

fun fibonacciNumberAtModulo(position: BigInteger, number: Int): BigInteger {
    if (number == 0) {
        return fibonacciNumberAt(position.toInt())
    } else if (number == 1) {
        return BigInteger.ZERO
    } else {
        val s = mutableListOf<BigInteger>(BigInteger.ZERO, BigInteger.ONE)
        var idx: Int = 0
        while (!(idx > 0 && s[idx] == BigInteger.ZERO && s[idx + 1] == BigInteger.ONE)) {
            s.add(((s[idx] % number.toBigInteger() + s[idx + 1] % number.toBigInteger()) % number.toBigInteger()))
            idx++
        }
        return s[(position % idx.toBigInteger()).toInt()]
    }
}

fun lastDigitOfSumOfFibonacciNumbersTill(limit: Int): Int {
    var sum:BigInteger = BigInteger.ZERO
    val fibonacci = mutableListOf<BigInteger>(BigInteger.ZERO, BigInteger.ONE)
    (0..limit).forEach {
        if (it > 1) {
            fibonacci[1] = fibonacci[0] + fibonacci[1]
            fibonacci[0] = fibonacci[1] - fibonacci[0]
            sum += fibonacci[1] % BigInteger.TEN
        } else {
            sum += fibonacci[it]
        }
    }
    return (sum % BigInteger.TEN).toInt()
}

fun lastDigitOfPartialSumOfFibonacciNumbers(start: Int, end: Int): Int {
    var sum:BigInteger = BigInteger.ZERO
    val fibonacci = mutableListOf<BigInteger>(BigInteger.ZERO, BigInteger.ONE)
    (0..start - 1).forEach {
        if (it > 1) {
            fibonacci[1] = fibonacci[0] + fibonacci[1]
            fibonacci[0] = fibonacci[1] - fibonacci[0]
        }
    }
    (start..end).forEach {
        if (it > 1) {
            fibonacci[1] = fibonacci[0] + fibonacci[1]
            fibonacci[0] = fibonacci[1] - fibonacci[0]
            sum += fibonacci[1] % BigInteger.TEN
        } else {
            sum += fibonacci[it]
        }
    }
    return (sum % BigInteger.TEN).toInt()
}

fun gcdOf(number1: BigInteger, number2: BigInteger): BigInteger {
    var num1 = number1
    var num2 = number2
    while (num2 != BigInteger.ZERO) {
        val temp = num2
        num2 = num1 % num2
        num1 = temp
    }
    return num1
}

fun lcmOf(number1: BigInteger, number2: BigInteger): BigInteger {
    return number1 * number2 / gcdOf(number1, number2)
}