module.exports = {
  fizzBuzz: function (value) {
    if (value == 1) {
      return "1";
    } else if (value == 2) {
      return "2";
    } else if (value % 5 == 0 && value % 3 == 0) {
      return "FizzBuzz";
    } else if (value % 3 == 0) {
      return "Fizz";
    } else if (value % 5 == 0) {
      return "Buzz";
    }
  },
};
