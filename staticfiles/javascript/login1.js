const signUpBtn = document.getElementById('signUp');
const signInBtn = document.getElementById('signIn');
const container = document.getElementById('container');

signUpBtn.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

signInBtn.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});

function handleSignInClick(){
    document.getElementById("sign-in-button").addEventListener("click", handleSignInClick);
    alert("Sign in button clicked!");
}

function handleSignUpClick(){
    document.getElementById("sign-in-button").addEventListener("click", handleSignInClick);
    alert("Sign in button clicked!");
}