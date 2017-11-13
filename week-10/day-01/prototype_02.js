function Rectangle(a_side, b_side) {
    this.a_side = a_side;
    this.b_side = b_side;
}

Rectangle.prototype.getArea = function() {
    return this.a_side * this.b_side;
}

let smallRect = new Rectangle(3, 4);

console.log(smallRect.getArea());

Rectangle.prototype.Circumference = function() {
    return (this.a_side + this.b_side) * 2;
}

console.log(smallRect.Circumference());