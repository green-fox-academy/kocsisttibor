class elevatorView {}
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
