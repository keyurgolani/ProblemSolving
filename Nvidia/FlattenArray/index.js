exports.flatten = (input) => {
    // Is it a type of object and is it an array?
    if (typeof input == "object" && Array.isArray(input))
        // If so, then flatten it
        return flattenArray(input)
    else
        // Otherwise return the input as it is
        return input
}

flattenArray = (element) => {
    var answer = [];
    for (let i = 0; i < element.length; i++) {
        if (typeof element[i] == "object" && Array.isArray(element[i])) {
            var otherAnswer = flattenArray(element[i])
            for (let j = 0; j < otherAnswer.length; j++)
                answer.push(otherAnswer[j])
        } else
            answer.push(element[i])
    }
    return answer
}