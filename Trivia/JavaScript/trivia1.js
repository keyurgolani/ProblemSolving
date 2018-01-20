const dynamicVariable = {
    currentVal: 0,
    valueOf: function() {
        return this.currentVal += 1
    }
}
exports.a = dynamicVariable