class exercises {

    sums(elements) {
        let sums = 0;
        elements.forEach(function(x) {
            sums += x;
        })
        return sums;
    }
}

let exer = new exercises()

module.exports = exer.sums;