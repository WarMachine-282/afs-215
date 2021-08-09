const fizzbuzz = require("../fizzbuzz").fizzbuzz
const assert = require('chai').assert

describe ("fizzbuzzkata", () => {
    it("Result should be 1", () => { 
    let result = fizzbuzz(1)
    assert.equal(result, "1")
})
it("Result should be 2", () => { 
    let result = fizzbuzz(2)
    assert.equal(result, "2")
})
it("Should return Fizzbuzz", () => { 
    let result = fizzbuzz(1)
    assert.typeOf(result, "string")
})
})