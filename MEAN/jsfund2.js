function Summer(x,y){
    sum = 0;
    for (x; x <= y; x++) {
        sum+=x;
    }
    console.log(sum);
}
Summer(1,2);

function min(arr){
    min = arr[0];
    for(var i = 0; i < arr.length; i++){
        if (arr[i] < min){
            min = arr[i];
        }
    }
    return console.log(min)
}
min([1,2,3,-1])

function average(arr){
    sum = 0;
    for (var i = 0; i < arr.length; i++){
        sum+=arr[i]
    }
    return console.log (sum/arr.length);
}
average([1,2,3]);

var Person = {
    name: 'Scott',
    distance_traveled: 0,
    say_name: function(){
        console.log(this.name);
    },
    say_something: function(phrase){
        console.log(this.name + " says " + phrase)
    },
    walk: function(){
        console.log(this.name +" is walking");
        this.distance_traveled=+3

        console.log(this.name+ " has traveled " + this.distance_traveled + " miles");
        return this;
    },
    run: function(){
        console.log(this.name+" is running!")
        this.distance_traveled+=10;
        console.log(this.name+ " has traveled " + this.distance_traveled + " miles");
        return this;
    },
    crawl: function(){
        console.log(this.name+" is crawling....")
        this.distance_traveled+=1
        console.log(this.name+ " has traveled " + this.distance_traveled + " miles");
        return this;
    }
}

Person.say_name();
Person.say_something('hello');
Person.walk().run().crawl().run()
