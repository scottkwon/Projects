// Will print numbers from start to end skipping by an integer we specify.
function printRange (start,end,skip) {
  for ( var i = start; i < end; start+=skip) {
    console.log (i);
  }
}

printRange (1,100,2)
