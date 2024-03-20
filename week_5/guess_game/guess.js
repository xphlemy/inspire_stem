const randomnumber =Math.floor(Math.random() * 100 ) +1;
console.log(randomnumber)
let attempt = 0;

function checkguess(){
    const gess = parseInt (document.getElementById("guessField").value)
    attempt++;
    if(isNaN(guess ) || guess < 1 || guess > 100){
        setMessage("please enter a valid number between 1 and 100")
        return;
}
    (ifguess === randomnumber){
        setMessage("Congragulations! Guessed correctly")
        document.getElementById("guessField").disabled = true;
    }else if(guess < randomnumber){
        setMessage("Too low try again")
    }else{
        setMessage("Too high, try again")
    }
}
        
    }
} 