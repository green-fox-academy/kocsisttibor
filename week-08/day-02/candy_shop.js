var candyButton = document.querySelector('.create-candies');
var candyNumber = 0;
var candyDisplay = document.querySelector('.candies');
var lollyButton = document.querySelector('.buy-lollypops');
var lollyNumber = 0;
var lollyDisplay = document.querySelector('.lollypops');
var automatCreation = false;
var rateDisplay = document.querySelector('.speed');
var rainButton = document.querySelector('.candy-machine');
var accelerator = 1;
var goalReached = false;
var candiesPerLolly = 10;
var lolliesToAccelerate = 1
var candyGoal = 30

function createCandy() {
    rate = (lollyNumber - lollyNumber % lolliesToAccelerate) / lolliesToAccelerate * accelerator;
    candyNumber += rate
    candyDisplay.textContent = candyNumber;
    rateDisplay.textContent = rate;
    if (candyNumber >= candyGoal && goalReached === false) {
        goalReached = true;
        automatCandy()
    }
}

function automatCandy() {
    if (goalReached === true) {
        console.log('stopping interval'); // reaches this point, but does not stops the timer with next line
        clearInterval(candyFactory);
    } else {
        var candyFactory = setInterval(createCandy, 1000);
    }
}

candyButton.addEventListener('click', function() {
    candyNumber += 1;
    candyDisplay.textContent = candyNumber;
});

lollyButton.addEventListener('click', function() {
    if (candyNumber >= candiesPerLolly) {
        lollyNumber += 1;
        candyNumber -= candiesPerLolly;
        lollyDisplay.textContent = '🍭'.repeat(lollyNumber);
        if (automatCreation === false) {
            automatCreation = true;
            automatCandy();
        }
    }
})

rainButton.addEventListener('click', function() {
    accelerator *= 10;
    rainButton.disabled = true;
})
