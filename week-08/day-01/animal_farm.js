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

