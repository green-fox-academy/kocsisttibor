class exercises {

    sums(elements) {
        if (elements !== null){
            let sums = 0;
            elements.forEach(function(x) {
                sums += x;
            })
            return sums;
        } 
    }
}

let exer = new exercises()

console.log(exer.sums(null))


module.exports = exer.sums;
