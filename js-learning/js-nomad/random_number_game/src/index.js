//parseInt doesn't work so well because of it's radix!
//should look like parseInt(var, 10) for decimal system

const numberForm = document.querySelector("#number-form");
const numberInput = numberForm.querySelector("input");
const guessForm = document.querySelector("#guess-form");
const guessInput = guessForm.querySelector("input");
const gameResult = document.querySelector("#game-result");
const gameWin = document.querySelector("#game-win");
const HIDDEN_CLASSNAME = "hidden";
let numberlimit = undefined;

function setNumberLimit(event) {
  event.preventDefault();
  numberlimit = numberInput.value;
}

function generateRandomNumber(event) {
  event.preventDefault();
  let numberguess = parseInt(guessInput.value);
  numberlimit = parseInt(numberlimit);
  if (!isNaN(numberlimit)&&numberguess<=numberlimit) {
    let rawRandomNumber = Math.random() * numberlimit;
    let randomNumber = Math.ceil(rawRandomNumber);
    paintResult(numberguess, randomNumber);
  }
}

function paintResult(numberguess, randomNumber) {
  gameResult.innerText = `You chose : ${numberguess}, the machine chose: ${randomNumber}.`;

  if (numberguess === randomNumber) {
    //you win
    gameWin.innerText = "You won!";
  } else {
    //you lose
    gameWin.innerText = "You lost!";
  }

  gameResult.classList.remove(HIDDEN_CLASSNAME);
  gameWin.classList.remove(HIDDEN_CLASSNAME);
}

numberForm.addEventListener("input", setNumberLimit);
guessForm.addEventListener("submit", generateRandomNumber);
