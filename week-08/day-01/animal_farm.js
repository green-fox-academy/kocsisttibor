class Animal {

    constructor() {
        this.hunger = 5;
        this.thirst = 5;
    }

    eat() {
        this.hunger -= 1;
    }

    drink() {
        this.thirst -= 1;
    }

    play() {
        this.hunger += 1;
        this.thirst += 1;
    }
}

let animal = new Animal();

class Farm {

    constructor(number) {
        this.listOfAnimals = [];
        this.maxOfAnimals = number
        for (let i = 1; i <= number; i += 1) {
            this.listOfAnimals.push(animal);
        }
    }

    breed() {
        if (this.listOfAnimals.length < this.maxOfAnimals) {
            this.listOfAnimals.push(animal);
        }
    }

    slaughter() {
        let hungers = [];
        this.listOfAnimals.forEach(function(e) {
            hungers.push(e.hunger);
        })
        this.listOfAnimals.splice(hungers.indexOf(Math.min(...hungers)), 1);
    }
}

let farm = new Farm(5);
farm.listOfAnimals[0].eat()
// console.log(farm);
farm.slaughter();
// console.log(farm);