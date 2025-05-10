
'use strict';
function get_object() {

    var theObject = {};

    var num = parseInt(prompt('Введите число от 0 до 999: '));

    if (num > 999) {
        console.log('Число больше 999');
    }

    var units = num % 10;
    var tens = ((num - units) % 100) / 10;
    var hundreds = (num - tens * 10 - units) / 100;

    theObject.units = units;
    theObject.tens = tens;
    theObject.hundreds = hundreds;

    return theObject;
}

console.log(get_object());