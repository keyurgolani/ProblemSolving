flattenarray = require('./index')
expect = require('chai').expect

let input1 = [
    1,
    2,
    4.5,
    "This is String",
    ["ABC", "xyz", 1, 5, [4, "Something", {
        "name" : "Keyur",
        "age": 27,
        "Gender": "Male"
    }, [4, 5, 3], "Last"], 5, {
        "a": 1,
        "b": 2,
        "c": [3, 4, 5]
    }, "Something"],
    "Final"
]
let output1 = [1,2,4.5,"This is String","ABC","xyz",1,5,4,"Something",{"name":"Keyur","age":27,"Gender":"Male"},4,5,3,"Last",5,{"a":1,"b":2,"c":[3,4,5]},"Something","Final"]
expect(JSON.stringify(flattenarray.flatten(input1))).equal(JSON.stringify(output1))

let input2 = [
    1, 
    {
        a: [2, [3]]
    }, 
    4, 
    [5, [6]], 
    [[7], 8, 9], 
    10
]
let output2 = [1,{"a":[2,[3]]},4,5,6,7,8,9,10]
expect(JSON.stringify(flattenarray.flatten(input2))).equal(JSON.stringify(output2))