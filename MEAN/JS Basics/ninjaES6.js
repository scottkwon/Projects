class Ninja {
    constructor(name){
        this.name = name;
        this.health = 100;
        this.speed = 3;
        this.strength = 3;
    }
    sayName(){
        console.log("Hello, my name is "+this.name)
    }

    showStats(){
        console.log("Name:" + this.name + ", " + "Health:" + this.health + ", " + "Speed:" + this.speed + ", " + "Strength:" + this.strength)
    }

    drinkSake(){
        this.health+=10
        console.log("Gained 10HP!")
    }
}

class Sensei extends Ninja {
    constructor(name){
        super(name)
        this.health = 200;
        this.speed = 10;
        this.strength = 10;
        this.wisdom = 10;
    }

    drinkSake(){
        this.health+=10
        console.log("Gained 10HP!")
    }

    speakWisdom(){
        this.drinkSake()
        console.log(this.health)
        console.log("YAAAH! SO WISSE")
    }

}

var scott = new Sensei('scott');
console.log(scott);
scott.speakWisdom();
scott.showStats();