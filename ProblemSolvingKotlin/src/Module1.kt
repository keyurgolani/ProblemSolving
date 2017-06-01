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