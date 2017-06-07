var _ = {
   map: function(arr,callback) {
      newlist=[];
      for (var i = 0; i < arr.length; i++){
        callback(arr[i]);
        if (callback(arr[i])){
          newlist.push(callback(arr[i]));
        }
     }
     return newlist;
   },
   reduce: function(arr, callback, memo) {
      var start = 0;
      if (memo == undefined){
         memo = arr[0];
         start = 1;
      }
      for (var i = start; i < arr.length; i++){
         callback(arr[i], memo);
         memo = callback(arr[i], memo);
      }
      return memo;
      },
   find: function(arr, callback) {
      for (var i = 0; i < arr.length; i++){
        callback(arr[i]);
        if (callback(arr[i])){
          return arr[i];
          break;
        }
     }
     return false;
   },
   filter: function(arr,callback) {
      newlist = [];
      for (var i = 0; i < arr.length; i++){
         callback(arr[i]);
         if (callback(arr[i])){
            newlist.push(arr[i]);
         }
      }
      return newlist;
   },
   reject: function(arr,callback) {
      newlist = [];
      for (var i = 0; i < arr.length; i++){
         callback(arr[i]);
         if (!callback(arr[i])){
            newlist.push(arr[i]);
         }
      }
      return newlist;
   }
 }
// you just created a library with 5 methods!
var evens = _.filter([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(evens)
var even = _.find([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(even)
var mult3 = _.map([1, 2, 3], function(num){ return num * 3; });
console.log(mult3)
var sum = _.reduce([1, 2, 3], function(memo, num){ return memo + num; }, 0);
console.log(sum)
var odds = _.reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(odds)
