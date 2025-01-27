let optionsSmall = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y", "z", "q", "w", "x"];
let optionsBig = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "Y", "Z", "Q", "W", "X"];
let optionsNumber = [0,1,2,3,4,5,6,7,8,9];
let optionsOther = ["/","*","#","@","&","-","_","?","=",">","&lt","!"];

let optionsAll = optionsSmall.concat(optionsNumber,optionsBig,optionsOther);  

function password(){
    let yourDigit = 0;
    let youCharacters = document.getElementById("charaters").value;
    yourDigit =+ document.getElementById("digit").value;
    let characterLength = youCharacters.length;
    let randomPassword = youCharacters;
    for(let i = 0; i < yourDigit - characterLength; i++){
        let randomNum = Math.random()*optionsAll.length;
        randomPassword += optionsAll[Math.floor(randomNum)];
    }  

    if(yourDigit < 1){
        document.getElementById('progressbarDiv').style.width = "1%";
        document.getElementById('progressbarDiv').style.backgroundColor = "black";
        document.getElementById('progressbarP').style.color = "black";
        document.getElementById('progressbarP').innerHTML = "The security value of your password: Nothing";
    }else if(yourDigit  < 4){
        document.getElementById('progressbarDiv').style.width = "5%";
        document.getElementById('progressbarDiv').style.backgroundColor = "red";
        document.getElementById('progressbarP').style.color = "red";
        document.getElementById('progressbarP').innerHTML = "The security value of your password: Very Low";
    }else if (yourDigit < 7){
        document.getElementById('progressbarDiv').style.width = "35%";
        document.getElementById('progressbarDiv').style.backgroundColor = "hotpink";
        document.getElementById('progressbarP').style.color = "hotpink";
        document.getElementById('progressbarP').innerHTML = "The security value of your password: Low";
    }else if (yourDigit < 9){
        document.getElementById('progressbarDiv').style.width = "55%";
        document.getElementById('progressbarDiv').style.backgroundColor = "yellow";
        document.getElementById('progressbarP').style.color = "yellow";
        document.getElementById('progressbarP').innerHTML = "The security value of your password: Standart";
    }else if (yourDigit < 11){
        document.getElementById('progressbarDiv').style.width = "75%";
        document.getElementById('progressbarDiv').style.backgroundColor = "turquoise";
        document.getElementById('progressbarP').style.color = "turquoise";
        document.getElementById('progressbarP').innerHTML = "The security value of your password: Strong";
    }else{
        document.getElementById('progressbarDiv').style.width = "96%";
        document.getElementById('progressbarDiv').style.backgroundColor = "limegreen";
        document.getElementById('progressbarP').style.color = "limegreen";
        document.getElementById('progressbarP').innerHTML = "The security value of your password: Very Strong";
    }
        console.log(yourDigit);
        return randomPassword;
    }

document.getElementById('button').addEventListener("click",function() {
    document.getElementById('out').innerHTML = password();
    document.getElementById('tooltiptext').innerHTML = "Password Copied";
});

       //Copy
function copyToClipboard(id) {
        var from = document.getElementById(id);
        var range = document.createRange();
        window.getSelection().removeAllRanges();
        range.selectNode(from);
        window.getSelection().addRange(range);
        document.execCommand('copy');
        window.getSelection().removeAllRanges();
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


