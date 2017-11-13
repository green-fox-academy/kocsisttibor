function Animal(sound) {
    this.sound = sound;
}

Animal.prototype.say = function() {
    console.log(this.sound);
}

let cat = new Animal('meow');

cat.say();

let dog = new Animal('woof');

dog.say();