let playerPosition = 0, bot1Position = 0, bot2Position = 0;
let currentQuestion = {};
let gameActive = false;
let timerInterval;
let timeLeft = 20;

async function fetchQuestion() {
    try {
        const response = await fetch('/api/question');
        const question = await response.json();
        return question;
    } catch (error) {
        console.error('Error fetching question:', error);
        return null;
    }
}

function startTimer() {
    timeLeft = 20;
    document.getElementById('timer').textContent = timeLeft;
    
    clearInterval(timerInterval);
    timerInterval = setInterval(() => {
        timeLeft--;
        document.getElementById('timer').textContent = timeLeft;
        
        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            handleTimeout();
        }
    }, 1000);
}

function handleTimeout() {
    if (gameActive) {
        document.getElementById('status').textContent = "Time's up! Moving backwards.";
        document.getElementById('status').className = 'alert alert-danger';
        playerPosition = Math.max(0, playerPosition - 1);
        moveCar("player-car", playerPosition);
        nextQuestion();
    }
}

async function startGame() {
    gameActive = true;
    playerPosition = bot1Position = bot2Position = 0;
    moveCar("player-car", 0);
    moveCar("bot1-car", 0);
    moveCar("bot2-car", 0);
    
    document.getElementById('startBtn').disabled = true;
    document.getElementById('status').className = 'alert alert-info d-none';
    await nextQuestion();
}

async function nextQuestion() {
    if (playerPosition >= 10) return endGame("Congratulations! You win!");
    if (bot1Position >= 10) return endGame("Bot 1 wins!");
    if (bot2Position >= 10) return endGame("Bot 2 wins!");

    currentQuestion = await fetchQuestion();
    if (currentQuestion) {
        document.getElementById("question").textContent = currentQuestion.question;
        document.getElementById("answer").value = "";
        document.getElementById("answer").focus();
        startTimer();
    }
}

function checkAnswer() {
    if (!gameActive) return;
    
    clearInterval(timerInterval);
    const userAnswer = document.getElementById("answer").value.trim();
    const statusElement = document.getElementById("status");
    statusElement.className = 'alert';
    
    if (userAnswer.toLowerCase() === currentQuestion.answer.toLowerCase()) {
        playerPosition++;
        moveCar("player-car", playerPosition);
        statusElement.textContent = "Correct! Moving forward.";
        statusElement.className += ' alert-success';
    } else {
        playerPosition = Math.max(0, playerPosition - 1);
        moveCar("player-car", playerPosition);
        statusElement.textContent = `Wrong! The correct answer was: ${currentQuestion.answer}`;
        statusElement.className += ' alert-danger';
    }

    // Smarter bot AI - higher chance of correct answer
    bot1Position += Math.random() > 0.3 ? 1 : -1;
    bot2Position += Math.random() > 0.3 ? 1 : -1;
    
    bot1Position = Math.max(0, Math.min(10, bot1Position));
    bot2Position = Math.max(0, Math.min(10, bot2Position));
    
    moveCar("bot1-car", bot1Position);
    moveCar("bot2-car", bot2Position);

    nextQuestion();
}

function moveCar(carId, position) {
    const car = document.getElementById(carId);
    const trackWidth = document.querySelector('.race-track').clientWidth;
    const progress = (position / 10) * (trackWidth - 100);
    car.style.left = `${progress}px`;
}

function endGame(message) {
    gameActive = false;
    clearInterval(timerInterval);
    document.getElementById("question").textContent = message;
    document.getElementById('startBtn').disabled = false;
    const statusElement = document.getElementById("status");
    statusElement.textContent = "Game Over!";
    statusElement.className = 'alert alert-info';
}

// Handle enter key press
document.getElementById('answer').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        checkAnswer();
    }
});
