// parent Dot class
class Dot {
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
    showLocation(){
        console.log(`This Dot is at x ${this.x} and y ${this.y}`);
    }
}
// child Circle class
class Circle extends Dot {
    constructor(x, y, radius){
        super(x, y);
        this.radius = radius
    }
    showLocation(){
        console.log(`This Circle is at x ${this.x} and y ${this.y}`);
    }
}

let circle1 = new Circle(33, 33, 33);
console.log(circle1);
circle1.showLocation();