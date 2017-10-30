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
        this.listOfAnimals.forEach(function(e, i) {
            let fattest_index = 0;
            let hunger = this.listOfAnimals[0].hunger;
            if (e.hunger < hunger) {
                hunger = e.hunger;
                fattest_index = i;
            }
        }.bind(this))
        this.listOfAnimals.splice(i, 1);
    }
}

let farm = new Farm(5);
farm.listOfAnimals[0].eat()
// console.log(farm);
farm.slaughter();
// console.log(farm);