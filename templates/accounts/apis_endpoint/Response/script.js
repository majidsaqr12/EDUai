function openModal() {
    document.getElementById("quiz-modal").style.display = "flex";
}

function closeModal() {
    document.getElementById("quiz-modal").style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById("quiz-modal");
    if (event.target == modal) {
        closeModal();
    }
}

async function generateQuiz() {
    const numQuestions = document.getElementById("num-questions").value;
    const questionType = document.getElementById("question-type").value;

    if (!numQuestions || !questionType) {
        alert("Please select both Number of Questions and Question Type.");
        return;
    }

    const courseId = localStorage.getItem('courseId');
    const studentId = localStorage.getItem('studentId');

    if (!courseId || !studentId) {
        alert("Course ID or Student ID not found. Please ensure you are logged in and have selected a course.");
        return;
    }

    //if statement
    const endpoint = Number(courseId) === 614 
    ? "https://aifr-svc.eduai.tech/query" 
    : Number(courseId) === 609 
    ? "https://aien-svc.eduai.tech/query" 
    : "https://aiar-svc.eduai.tech/query";

    const formData = new FormData();
    formData.append("num_questions", numQuestions);
    formData.append("question_type", questionType);
    formData.append("courseId", courseId);
    formData.append("studentId", studentId);

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const responseData = await response.json();

        console.log("Quiz Generated Successfully:", responseData);
        localStorage.setItem('quizQuestions', JSON.stringify(responseData.questions));
        window.location.href = '/templates/accounts/apis_endpoint/Quiz/index.html';
        closeModal();

    } catch (error) {
        console.error("Error generating quiz:", error);
        alert("There was an error generating the quiz. Please try again.");
    }
}

function loadChatResponse() {
    const question = localStorage.getItem('chatQuestion') || 'What are the layers of the atmosphere?';
    const response = localStorage.getItem('chatResponse') || 'Default response if not found';

    document.getElementById('question-text').textContent = question;

    const responseContentDiv = document.getElementById('response-content');
    responseContentDiv.innerHTML = response;
}

window.onload = loadChatResponse;
