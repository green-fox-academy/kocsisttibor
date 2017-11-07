'use strict'

class elevatorView {

    constructor(maxLevels) {
        this.drawLevels(maxLevels);
    }

    drawLevels(maxLevels) {
        for (let i = maxLevels; i > 0; i -= 1) {
            let div = document.createElement('div');
            div.classList.add('level_' + i)
            let floors = document.querySelector('div.floors');
            floors.appendChild(div);
        }
    }

    displayPeople(actualLevel, actualPeople, maxLevels) {
        let divs = document.querySelectorAll('div.floors > div');
        divs.forEach(function(div) {
            div.textContent = ""
        });
        divs[maxLevels - actualLevel].textContent = actualPeople;
    }
}

class elevatorModel {
    
    constructor(maxLevels, maxPeople) {
        this.maxPeople = maxPeople;
        this.maxLevels = maxLevels;
        this.actualLevel = 1;
        this.actualPeople = 0;
    }
    
    addPeople() {
        if (this.actualPeople < this.maxPeople) {
            this.actualPeople += 1;
        }
    }
    
    removePeople() {
        if (this.actualPeople > 0) {
            this.actualPeople -= 1;
        }
    }

    levelUp() {
        if (this.actualLevel < this.maxLevels) {
            this.actualLevel += 1;
        }
    }

    levelDown() {
        if (this.actualLevel > 1) {
            this.actualLevel -= 1;
        }
    }
}
class elevatorController {

    constructor(maxLevels, maxPeople) {
        this.model = new elevatorModel(maxLevels, maxPeople);
        this.view = new elevatorView(maxLevels);
        this.view.displayPeople(this.model.actualLevel, this.model.actualPeople, this.model.maxLevels);
        this.up();
        this.down();
    }

    up() {
        let up = document.querySelector('button.up');
        up.addEventListener('click', function() {
            this.model.levelUp();
            this.view.displayPeople(this.model.actualLevel, this.model.actualPeople, this.model.maxLevels);
        }.bind(this))   //the eventlistener changed the this, so here should be "bound back"
    }

    down() {
        let down = document.querySelector('button.down');
        down.addEventListener('click', function() {
            this.model.levelDown();
            this.view.displayPeople(this.model.actualLevel, this.model.actualPeople, this.model.maxLevels);
        }.bind(this))
    }
}

let elevator = new elevatorController(10, 5);
