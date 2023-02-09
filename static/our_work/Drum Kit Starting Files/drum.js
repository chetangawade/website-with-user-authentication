// event listner in js
// addEventListener
//document.querySelector("button").addEventListener("click",handleClick()) This is straingt up menthod call
var lenghts = document.querySelectorAll(".drum").length;
for (var i = 0; i < lenghts; i++) {
    document.querySelectorAll(".drum")[i].addEventListener("click", function () {
        var buttonInnerHTML = this.innerHTML;
        makeSound(buttonInnerHTML);
        makeBlur(buttonInnerHTML);
    }
    )
}

// keyboard event listnear
document.addEventListener("keypress", function (event) {
    makeSound(event.key);
    makeBlur(event.key);
})

// ALL in one function;
function makeSound(key) {
    switch (key) {
        case "w":
            var ton1 = new Audio('sounds/tom-1.mp3');
            ton1.play();
            break;
        case "a":
            var ton2 = new Audio('sounds/tom-2.mp3');
            ton2.play();
            break;
        case "s":
            var ton3 = new Audio('sounds/tom-3.mp3');
            ton3.play();
            break;
        case "d":
            var ton4 = new Audio('sounds/tom-4.mp3');
            ton4.play();
            break;
        case "j":
            var snare = new Audio('sounds/snare.mp3');
            snare.play();
            break;
        case "k":
            var crash = new Audio('sounds/crash.mp3');
            crash.play();
            break;
        case "l":
            var kick = new Audio('sounds/kick-bass.mp3');
            kick.play();
            break;
        default:
            console.log("buttonInnerHTML");
    }
}


// making show to the photo of the sound which is activated
function makeBlur(key){
    var activationButton = document.querySelector("."+key);
    activationButton.classList.add("pressed");
    setTimeout(function(){
        activationButton.classList.remove("pressed");
    },100);

}