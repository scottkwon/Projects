function Ninja(name){
    var self = this;
    var speed = 3;
    var strength = 3;

    this.name = name;
    this.health = 100;
    this.sayName = function(){
        console.log(this.name)
    }
    this.drinkSake = function(){
        this.health+=10
    }
    this.showStats = function(){
        console.log("Name:" + this.name + ", " + "Health:" + this.health + ", " + "Speed:" + speed + ", " + "Strength:" + strength)
    }
    this.punch = function(ninja){
        if(ninja instanceof Ninja){
            ninja.health -= 5 
            console.log(ninja.name + " was punched by " + this.name + " and lost 5 health!")
        } else {
            console.log("You can only punch ninjas!")
        }
    }
    this.kick = function(ninja){
        if(ninja instanceof Ninja){
            ninja.health -= 5 * ninja.strength
            console.log(ninja.name + " was kicked by " + this.name + " and lost 15 health!")
        } else {
            console.log("You can only kick ninjas!")
        }
    }
    return this
}
