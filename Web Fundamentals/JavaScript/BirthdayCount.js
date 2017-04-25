//Counts down to your birthday, displaying different messages the closer you get.

function bdayCount (num) {
  for (var i = num; i >= 0; i--) {
    if (i > 30) {
      console.log (i +" days until my birthday. Such a long time.. :(");
    } else if (i > 5) {
      console.log ("Less than a month left." + i + " until my Birthday!");
    } else if ( i > 0 ) {
      console.log (i + " DAYS UNTIL MY BIRTHDAY!!");
    } else {
      console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*");
      console.log("♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪");
      console.log("*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«");
    }
  }
}

bdayCount(60);
