const expect = require("chai").expect;
const Fizzbuzzkata = require("../fizzbuzzkata");

describe(fizzbuzz, function () {
  it("can call a fizzbuzz", function () {
    fizzBuzz(1);
  });

  it("returns 1 when 1 passed in", function () {
    const result = fizzBuzz(1);
    expect.equal("1");
  });

  it("returns 2 when 2 passed in", function () {
    const result = fizzBuzz(2);
    expect.equal("2");
  });

  it("returns Fizz when 6 passed in", function () {
    const result = fizzBuzz(6);
    expect.equal("Fizz");
  });

  it("returns Buzz when 10 passed in", function () {
    const result = fizzBuzz(10);
    expect.equal("Buzz");
  });
  it("returns FizzBuzz when 15 passed in", function () {
    const result = fizzBuzz(15);
    expect.equal("FizzBuzz");
  });
});
