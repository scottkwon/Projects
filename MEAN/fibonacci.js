function fib() {
  var num = 1
  var memo = 0
  function nacci() {
    var x = num + memo
    console.log(x)
    memo = num;
    num = x;
  }
  return nacci;
}
var fibCounter = fib();
fibCounter() // "1"
fibCounter() // "2"
fibCounter() // "3"
fibCounter() // "5"
fibCounter() // "8"
fibCounter() // "13"
fibCounter() // "21"
fibCounter() // "34"
fibCounter()
