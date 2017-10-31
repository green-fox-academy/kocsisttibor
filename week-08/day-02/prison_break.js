// Create a prison function, that has your name as a private fugutive variable
// The function should return an object that has two methods:
//  - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//  - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable


function prison(name) {
    var times = 0;
    var fugitive = [name];
    function visit() {
        times += 1
        if (fugitive.length === 0) {
            console.log('Nobody is here anymore');
        } else {
            console.log(fugitive[0]+ ' is visited ' + times + ' times');
        }
    }
    function escape() {
        console.log('BREAKING NEWS, ' + fugitive[0] + ' escaped the prison')
        fugitive.splice(0, 1);
    }
    return {
        visit: function() {
            visit();
        },
        escape: function() {
            escape();
        }
    }
}


const alcatraz = prison('Sad Panda'); //this kindof instantiates the function and makes it possible to use variables inside it

alcatraz.visit() // Sad Panda is visited 1 time(s)
alcatraz.visit() // Sad Panda is visited 2 time(s)
alcatraz.escape() // BREAKING NEWS, Sad Panda escaped the prison
alcatraz.visit() // Nobody is here anymore

prison('MIchael Scofield').visit(); //if the inner functions are called without creating first a variable assigned to the prison function, than the inner variable starts always from the basic value
prison('MIchael Scofield').visit();