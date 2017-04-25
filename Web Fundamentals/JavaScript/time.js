//Time teller. 


function whatTime (HOUR, MINUTE, PERIOD) {

  var LANGUAGE ;


  if (MINUTE > 30) {
    HOUR+=1;
    LANGUAGE="almost";
  } else if (MINUTE < 30) {
    LANGUAGE="just after";
  }

  if (PERIOD == "AM" || "am" || "Am") {
    PERIOD = "morning.";
  } else if (PERIOD == "PM" || "pm" || "Pm") {
    PERIOD = "evening.";
  } else if (HOUR == 12 && PERIOD == "AM" || "am" || "Am") {
    PERIOD="MIDNIGHT.";
  } else if (HOUR == 12 && PERIOD == "PM" || "am" || "Am") {
    PERIOD="NOON.";
  }

  console.log ("It is " + LANGUAGE + " " + HOUR + " in the " + PERIOD);
}

whatTime (8,50,"AM");
