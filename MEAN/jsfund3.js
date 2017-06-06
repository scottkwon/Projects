function Person(name) {
    this.name = name;
    this.distance_traveled = 0;
    this.say_name = function(){
        console.log(this.name);
        return this;
    };
    this.walk = function(){
        console.log(this.name +" is walking");
        this.distance_traveled+=3;
        console.log(this.name + " traveled "+ this.distance_traveled + " miles");
        return this;
    };
    this.run = function(){
        console.log(this.name +" is running!");
        this.distance_traveled+=10;
        console.log(this.name + " traveled "+ this.distance_traveled + " miles");
        return this;
    };
    this.crawl = function(){
        console.log(this.name +" is crawling");
        this.distance_traveled+=1;
        console.log(this.name + " traveled "+ this.distance_traveled + " miles");
        return this;
    };
}

var me = new Person('Scott')
me.say_name().walk().run().crawl().crawl();

function ninjaConstructor(name, cohort, belt_level){
    this.name=name;
    this.cohort=cohort;
    this.belt_level = 0;
    belts=['yellow','red','black'];
    this.levelup = function(){
        if (belt_level < 2){
            belt_level+=1;
            console.log('Leveled up! ' + this.name + ' is now a ' + belts[belt_level] + ' belt');
        } else {
            console.log('Already a Blackbelt!');
        }
        return this;
    }
}

var me = new ninjaConstructor('Scott', 'MEAN', 0);
me.levelup().levelup().levelup();
