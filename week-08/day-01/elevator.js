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
}

class elevatorModel {
    
    constructor(maxPeople, maxLevels) {
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
        this.view = new elevatorView(maxLevels);
        this.model = new elevatorModel(maxLevels, maxPeople);
    }
}

elevator = new elevatorController(10, 5);