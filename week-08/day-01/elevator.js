class elevatorView {

    drawLevels(maxLevels) {
        for (let i = maxLevels; i > 0; i -= 1) {
            let div = document.createElement('div');
            div.classList.add('level_' + i)
            let floors = document.querySelector('div.floors');
            floors.appendChild(div);
        }
    }
}

elevator = new elevatorView;
elevator.drawLevels(10);

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
}
class elevatorController {}
