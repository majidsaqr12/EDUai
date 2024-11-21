// Function to open the modal
function openModal() {
    document.getElementById("quiz-modal").style.display = "flex";
}

// Function to close the modal
function closeModal() {
    document.getElementById("quiz-modal").style.display = "none";
}

// Close modal when clicking outside the modal content
window.onclick = function(event) {
    var modal = document.getElementById("quiz-modal");
    if (event.target == modal) {
        closeModal();
    }
}

// Function to generate the quiz
async function generateQuiz() {
    const numQuestions = document.getElementById("num-questions").value;
    const questionType = document.getElementById("question-type").value;

    // Validate inputs
    if (!numQuestions || !questionType) {
        alert("Please select both Number of Questions and Question Type.");
        return;
    }

    // Retrieve courseId and studentId from localStorage
    const courseId = localStorage.getItem('courseId');
    const studentId = localStorage.getItem('studentId');

    if (!courseId || !studentId) {
        alert("Course ID or Student ID not found. Please ensure you are logged in and have selected a course.");
        return;
    }

    // Create a FormData object
    const formData = new FormData();
    formData.append("num_questions", numQuestions);
    formData.append("question_type", questionType);
    formData.append("courseId", courseId);
    formData.append("studentId", studentId);

    try {
        // Send POST request to the endpoint with FormData
        const response = await fetch("https://aiar-svc.eduai.tech/quiz", {
            method: "POST",
            body: formData
        });

        // Check if the response is OK
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        // Parse the JSON response if needed
        // Assuming the endpoint returns some confirmation or quiz data
        const responseData = await response.json();

        // For demonstration, we'll log the response data
        console.log("Quiz Generated Successfully:", responseData);
        localStorage.setItem('quizQuestions', JSON.stringify(responseData.questions));
        window.location.href = '/templates/accounts/apis_endpoint/Quiz/index.html';
        closeModal();

    } catch (error) {
        console.error("Error generating quiz:", error);
        alert("There was an error generating the quiz. Please try again.");
    }
}

// Function to load chat response and question from localStorage
function loadChatResponse() {
    // Retrieve the question and response from localStorage
    const question = localStorage.getItem('chatQuestion') || 'What are the layers of the atmosphere?';
    const response = localStorage.getItem('chatResponse') || 'Default response if not found';

    // Update the question text
    document.getElementById('question-text').textContent = question;

    // Update the response content
    const responseContentDiv = document.getElementById('response-content');
    responseContentDiv.innerHTML = response;
}

// Call the function when the page loads
window.onload = loadChatResponse;
