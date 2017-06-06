class Vehicle{
    constructor(name, wheels, numpassengers, speed){
        // private
        var self = this;
        var distance_traveled = 0;
        var updateDistanceTraveled = function(){
            console.log(distance_traveled+=speed);
            return self;
        }

        // public
        this.name=name;
        this.wheels=wheels;
        this.numpassengers=numpassengers;
        this.speed=speed;
        this.makeNoise = function(sound){
            console.log(sound);
            return this;
        };

        this.move = function(sound){
            updateDistanceTraveled();
            console.log("Distance traveled: " + distance_traveled + " miles")
            this.makeNoise(sound);
            return this;
        };

        this.checkMiles = function(){
            console.log(distance_traveled);
            return this;
        };

        this.generateVin = function(){
            var vnum = Math.random().toString(36).substring(7);
            console.log(vnum);
            return self;
        };
    }
}

var Bike = new Vehicle("Bike", 2, 2, 5);
Bike.move('ring,ring!').checkMiles().generateVin();
