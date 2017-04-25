//Starting with a penny, and doubling each day until num days.


function pennyDay(num) {
  var sum = 1;
  for (var i = 1; i <= num; i++) {
    sum = sum * 2;
  }
  return sum;
}

pennyDay(30);
