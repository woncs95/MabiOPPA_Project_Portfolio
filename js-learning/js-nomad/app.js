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

/*const age = parseInt(prompt("how old are you?"));

if (isNaN(age)) {
  alert("it's not a number");

  //if and&or
} else if ((age < 18 && age > 50) || false) {
  console.log("you can't drink");
  //age exactly 100
} else if (age === 100) {
  console.log("you are wise");
} else {
  console.log("you can drink");
}*/

//2. Interacting with Web

//we can use HTMl in JS
//document.title = html title
//document.body etc..

//grab id from document(HTML)
const title = document.getElementById("title");
console.log("getElementById: ");
console.dir(title);
title.innerText = "Got you!";
console.dir(title.id);
console.dir(title.className);
console.dir(title.innerText);

//grab class name from document
const somethings = document.getElementsByClassName("something");
console.log("getElementByClassName: ");
console.log(somethings);

//grab tag names
const hellow = document.getElementsByTagName("h1");
console.log("getElementByTagName: ");
console.log(hellow);

//search elements in css way (h1 inside of class with ".className")
//only returns one element
//if there are more classes with same names selector gives only first element
const helloQuery = document.querySelector(".hellow h1");
console.log("querySelector: ");
console.log(helloQuery);
console.dir(helloQuery);

//selector gives all elements they match
const helloQueryAll = document.querySelectorAll(".hellow h1");
console.log("querySelectorAll: ");
console.log(helloQueryAll);

//both give the same thing
const helloId = document.getElementById("hello");
const helloQueryId = document.querySelector("#hello");

////handling events(interacting if user does something)
const styleChanger = document.querySelector("div.hellow h1");
styleChanger.style.color = "red";
console.log("styleChanger.style: ");
console.dir(styleChanger.style);
//listen click event
function handleHellowClick() {
  const colorContainer = ["blue", "red"];
  switch (styleChanger.style.color) {
    case "red":
      styleChanger.style.color = colorContainer[0];
      styleChanger.style.fontSize = "x-large";
      break;
    case "blue":
      styleChanger.style.color = colorContainer[1];
      styleChanger.style.fontSize = "large";
      console.dir(styleChanger.style.fontSize);
      break;
  }
  console.log("title was clicked!");
}
styleChanger.addEventListener("click", handleHellowClick);

//advanced events listening

function handleMouseLeave() {
  styleChanger.innerText = "Mouse is gone!";
}
//same as above
styleChanger.onClick = handleHellowClick;
styleChanger.addEventListener("mouseleave", handleMouseLeave);

//addEventListener better
//because you can remove it with .removeListener

function handleWindowResize() {
  document.body.style.backgroundColor = "tomato";
}

function handleWindowCopy() {
  alert("copier!");
}
window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);

//Connection Events

function handleWindowOffline() {
  alert("SOS no WIFI");
}
function handleWindowOnline() {
  alert("WIFI is there again!");
}
window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline);

//CSS in JS(interacting js with css)
const cssChanger = document.querySelector(".changedByCss h1");

function handleTitleClick() {
  const activeClass = "active";
  if (cssChanger.className === activeClass) {
    cssChanger.className = "changingH1";
  } else {
    cssChanger.className = activeClass;
  }
}

//cssChanger.addEventListener("click", handleTitleClick);

//class list
function handleTitleClickinList() {
  const activeClass = "active";
  if (cssChanger.classList.contains(activeClass)) {
    cssChanger.classList.remove(activeClass);
  } else {
    cssChanger.classList.add = activeClass;
  }
}

cssChanger.addEventListener("click", handleTitleClickinList);