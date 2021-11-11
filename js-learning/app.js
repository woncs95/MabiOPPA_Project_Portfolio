const a = 5;
const b = 2;
let myName = "changseup";

//old method can't lock values like with const
var c = 4;

console.log(a + b);
console.log(myName);

myName = myName + "wyon";
console.log(myName);

//boolean
const amITall = false;
const amIFat = null;

//undefined
let something;

//data structure
const daysOfWeek = ["mon", " tue", "wed", "thu", "fri", "sat"];

//Get Item from Array
console.log(daysOfWeek[0]);

//Add one more day to the array
daysOfWeek.push("sun");
console.log(daysOfWeek);

//object (rules different inside object)
const player = {
  name: "chang",
  points: 10,
  fat: true,
};
console.log(player);
console.log(player.name);
//you can change&add elements inside constant object
player.points = 20;
player.lastName = "potato";
console.log(player);

function sayHello(otherName) {
  //use Backtick for template string!!
  console.log(`Hello ${otherName}`);
}

sayHello("chang");

const calculator = {
  add: function (a, b) {
    return a + b;
  },
};

const addedNr = calculator.add(2, 5);
console.log(addedNr);

//get an input value & change value type

const age = parseInt(prompt("how old are you?"));

if (isNaN(age)) {
  alert("it's not a number");
  
  //if and&or
} else if (age < 18 && age > 50 || false) {
  console.log("you can't drink");
} else {
  console.log("you can drink");
}

