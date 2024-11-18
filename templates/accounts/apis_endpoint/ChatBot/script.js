// Retrieve stored studentId and courseId from localStorage
const studentId = localStorage.getItem('studentId');
const courseId = localStorage.getItem('courseId');

// Check if studentId and courseId are available
if (!studentId || !courseId) {
    alert('Student ID or Course ID is missing. Please select a subject again.');
    // Redirect to the subject selection page if needed
    // window.location.href = '/path/to/subject/selection/page.html';
}

// Get DOM elements
const submitButton = document.getElementById('submit-button');
const questionInput = document.getElementById('question-input');
const loadingSpinner = document.getElementById('loading-spinner');
const submitText = document.getElementById('submit-text');
const responseContainer = document.getElementById('response-container');

// Add event listener to the submit button
submitButton.addEventListener('click', function() {
    // Get the query from the textarea
    const query = questionInput.value.trim();

    if (!query) {
        alert('Please enter a question.');
        return;
    }

    // Show loading spinner
    loadingSpinner.style.display = 'inline-block';
    submitText.style.display = 'none';
    submitButton.disabled = true;

    // Construct FormData
    const formData = new FormData();
    formData.append('studentId', studentId);
    formData.append('courseId', courseId);
    formData.append('query_request', JSON.stringify({ query: query }));

    // Send POST request
    fetch('http://57.128.91.158/query/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading spinner
        loadingSpinner.style.display = 'none';
        submitText.style.display = 'inline';
        submitButton.disabled = false;

        // Display the response
        responseContainer.innerHTML = data.response || 'No response from server.';
    })
    .catch(error => {
        console.error('Error:', error);
        // Hide loading spinner
        loadingSpinner.style.display = 'none';
        submitText.style.display = 'inline';
        submitButton.disabled = false;
        responseContainer.innerHTML = 'An error occurred. Please try again.';
    });
});