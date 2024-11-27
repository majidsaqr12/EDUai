const subjectsData = [
    { id: 314, name: "Arabic" },
    { id: 614, name: "French" },
    { id: 316, name: "Physics" },
    { id: 317, name: "Biology" },
    { id: 318, name: "History" },
    { id: 319, name: "Science" },
    { id: 320, name: "Geography" },
    { id: 321, name: "Chemistry" },
    { id: 609, name: "English" },
    { id: 323, name: "Mathematics" }
  ];
  
  const subjectContainer = document.getElementById("subject-container");
  
  subjectsData.forEach(subject => {
    const subjectCard = document.createElement("div");
    subjectCard.className = "subject-item";
    subjectCard.innerHTML = `
      <div class="card" id="custom-card" onclick="sendSubjectData(${subject.id})">
        <div class="card-body">
          <div class="d-flex justify-content-between">
            <img src="images/icons/${subject.name.toLowerCase()}.png" alt="${subject.name} Icon" class="icon">
            <img src="images/icons/arrow.png" alt="Arrow Icon" class="icon">
          </div>
          <h5 id="custom-card-title" class="mt-3 text-start">${subject.name}</h5>
        </div>
      </div>
    `;
    subjectContainer.appendChild(subjectCard);
  });
  
  function sendSubjectData(subjectId) {
    const userId = 21;
    const formData = new FormData();
    formData.append('courseId', subjectId);
    formData.append('studentId', userId); 

  //if statement
  const endpoint = Number(courseId) === 614 
  ? "https://aifr-svc.eduai.tech/query" 
  : Number(courseId) === 609 
  ? "https://aien-svc.eduai.tech/query" 
  : "https://aiar-svc.eduai.tech/query";
  
    fetch(endpoint, {
      method: "POST",
      body: formData
    })
    .then(response => {
      console.log(response);
      localStorage.setItem('courseId', subjectId);
      localStorage.setItem('studentId', userId);
      window.location.href = '/templates/accounts/apis_endpoint/ChatBot/index.html';
    })
    .catch(error => console.error(error));
  }
  