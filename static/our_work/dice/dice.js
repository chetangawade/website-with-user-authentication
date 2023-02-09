// for images 1
var randNumber1 = Math.floor((Math.random() * 6) +1) ;
var randomImageSource1 = "images/dice" + randNumber1 + ".png";
var image1 = document.querySelectorAll("img")[0];
image1.setAttribute("src",randomImageSource1);
console.log(randomImageSource1);

// for images 2
var randNumber2 = Math.floor((Math.random() * 6) +1) ;
var randomImageSource2 = "images/dice" + randNumber2 + ".png";
var image2 = document.querySelectorAll("img")[1];
image2.setAttribute("src",randomImageSource2);
console.log(randomImageSource2);

//Resutls
if(randNumber1<randNumber2){
    document.querySelector("h1").innerHTML = "Player 2 win!";
}
else if (randNumber1>randNumber2){
    document.querySelector("h1").innerHTML = "Player 1 win!";
}
else{
    document.querySelector("h1").innerHTML = "Match Drawn !";
}