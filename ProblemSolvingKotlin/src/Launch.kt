/**
 * Created by keyurgolani on 6/1/17.
 */

fun main(args: Array<String>) {
    val values: List<Int>? = readLine()?.split(" ")?.map { it.toInt() }
    println(sumNumbers(values!!))
}