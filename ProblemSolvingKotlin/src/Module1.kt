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

fun  gcdOf(number1: Int, number2: Int): Any? {}

fun  lastDigitOfFibonacciNumberAt(position: Int): Any? {}

fun  fibonacciNumberAt(position: Int): Any? {}

fun  fibonacciSeriesTill(position: Int): Any {}