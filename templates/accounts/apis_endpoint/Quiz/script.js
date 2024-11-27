document.addEventListener('DOMContentLoaded', () => {
    renderQuiz();
    document.getElementById('confirm-button').addEventListener('click', submitQuiz);
});

function renderQuiz() {
    const quizContainer = document.getElementById('quiz-questions');
    const quizData = JSON.parse(localStorage.getItem('quizQuestions'));
    
    if (!quizData || !Array.isArray(quizData) || quizData.length === 0) {
        quizContainer.innerHTML = '<p>No quiz data available. Please generate a quiz first.</p>';
        document.getElementById('confirm-button').disabled = true;
        return;
    }

    quizData.forEach((q, index) => {
        const quizCard = document.createElement('div');
        quizCard.classList.add('quiz-card');

        const questionHeader = document.createElement('h5');
        questionHeader.textContent = `Question ${index + 1}`;
        quizCard.appendChild(questionHeader);

        const questionText = document.createElement('p');
        questionText.textContent = q.question;
        quizCard.appendChild(questionText);

        const optionsDiv = document.createElement('div');
        optionsDiv.classList.add('options');

        q.choices.forEach(choice => {
            const label = document.createElement('label');
            
            const input = document.createElement('input');
            input.type = 'radio';
            input.name = `question${index}`;
            input.value = choice;
            input.required = true;

            label.appendChild(input);
            label.appendChild(document.createTextNode(choice));

            optionsDiv.appendChild(label);
        });

        quizCard.appendChild(optionsDiv);
        quizContainer.appendChild(quizCard);
    });
}

function submitQuiz() {
    const quizData = JSON.parse(localStorage.getItem('quizQuestions'));
    const resultContainer = document.getElementById('result-container');
    const totalQuestions = quizData.length;
    let correctAnswers = 0;

    for (let i = 0; i < totalQuestions; i++) {
        const selectedOption = document.querySelector(`input[name="question${i}"]:checked`);
        if (selectedOption) {
            const userAnswer = selectedOption.value;
            const correctAnswer = quizData[i]['correct answer'];
            const selectedLabel = selectedOption.parentElement;
            
            if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
                selectedLabel.classList.add('correct-answer');
                correctAnswers++;
            } else {
                selectedLabel.classList.add('incorrect-answer');
                const allOptions = document.querySelectorAll(`input[name="question${i}"]`);
                allOptions.forEach(option => {
                    if (option.value.toLowerCase() === correctAnswer.toLowerCase()) {
                        option.parentElement.classList.add('correct-highlight');
                    }
                });
            }
        }
    }

    resultContainer.style.display = 'block';
    resultContainer.innerHTML = `
        <h4>Quiz Results</h4>
        <p>You answered <strong>${correctAnswers}</strong> out of <strong>${totalQuestions}</strong> questions correctly.</p>
    `;

    const allInputs = document.querySelectorAll('input[type="radio"]');
    allInputs.forEach(input => input.disabled = true);
    document.getElementById('confirm-button').disabled = true;
}