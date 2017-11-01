var candyButton = document.querySelector('.create-candies');
var candyNumber = 0;
var candyDisplay = document.querySelector('.candies');
var lollyButton = document.querySelector('.buy-lollypops');
var lollyNumber = 0;
var lollyDisplay = document.querySelector('.lollypops');

candyButton.addEventListener('click', function() {
    candyNumber += 1;
    candyDisplay.textContent = candyNumber;
});

lollyButton.addEventListener('click', function() {
    console.log(candyNumber)
    if (candyNumber >= 10) {
        lollyNumber += 1;
        candyNumber -= 10;
        console.log(lollyNumber)
        lollyDisplay.textContent = '🍭'.repeat(lollyNumber);
    }
})