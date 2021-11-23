// or
// const loginInput = document.querySelector("#login-form input");
// const loginButton = document.querySelector("#login-form button");

const loginForm = document.querySelector("#login-form");
const loginInput = loginForm.querySelector("input");
// const loginButton = loginForm.querySelector("button");

// function handleloginButtonClick() {
//   const username = loginInput.value;
//   if  username.length === 0) {
//     console.log("You have to write your name first");
//   }
//   else if username.length > 15){
//     alert("Your name is too long!");
//   }
//   else{
//     console.log("hello", username);
//   }
// }

// loginButton.addEventListener("click", handleloginButtonClick);
// or use html for the limitations!!

// now we need to handle "submit event"!4

const greeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";
function handleloginSubmit(event) {
  event.preventDefault(); //default behaviour of browser stops (i.e. not refreshing)
  loginForm.classList.add(HIDDEN_CLASSNAME);
  const username = loginInput.value;
  localStorage.setItem(USERNAME_KEY, username);
  paintGreetings(username);
}

function paintGreetings(username) {
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

const savedUsername = localStorage.getItem(USERNAME_KEY);

if (savedUsername === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", handleloginSubmit);
} else {
  paintGreetings(savedUsername);
}
// const link = document.createElement("a");

// function handleLinkClick(event) {
//   event.preventDefault();
//   console.log(loginInput.value);
// }
// link.addEventListener("click", handleLinkClick);

//localStorage
