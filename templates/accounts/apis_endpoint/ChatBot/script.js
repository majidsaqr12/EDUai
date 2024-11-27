const studentId = localStorage.getItem('studentId');
const courseId = localStorage.getItem('courseId');

if (!studentId || !courseId) {
    alert('Student ID or Course ID is missing. Please select a subject again.');
}

const submitButton = document.getElementById('submit-button');
const questionInput = document.getElementById('question-input');
const loadingSpinner = document.getElementById('loading-spinner');
const submitText = document.getElementById('submit-text');
const responseContainer = document.getElementById('response-container');

submitButton.addEventListener('click', function() {
    const query = questionInput.value.trim();

    if (!query) {
        alert('Please enter a question.');
        return;
    }

    loadingSpinner.style.display = 'inline-block';
    submitText.style.display = 'none';
    submitButton.disabled = true;

    const formData = new FormData();
    formData.append('studentId', studentId);
    formData.append('courseId', courseId);
    formData.append('query_request', JSON.stringify({ query: query }));

    //if statement
    const endpoint = courseId === 614 
    ? "https://aifr-svc.eduai.tech/query" 
    : courseId === 322 
    ? "https://aien-svc.eduai.tech/query" 
    : "https://aiar-svc.eduai.tech/query";

    fetch(endpoint, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) 
    .then(data => {
        loadingSpinner.style.display = 'none';
        submitText.style.display = 'inline';
        submitButton.disabled = false;
        localStorage.setItem('chatResponse', data.response );
        localStorage.setItem('chatQuestion', query );
        window.location.href = '/templates/accounts/apis_endpoint/Response/index.html';
        responseContainer.innerHTML = data.response || 'No response from server.';
    })
    .catch(error => {
        console.error('Error:', error);
        loadingSpinner.style.display = 'none';
        submitText.style.display = 'inline';
        submitButton.disabled = false;
        responseContainer.innerHTML = 'An error occurred. Please try again.';
    });
});