from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required

@login_required
def subjects_view(request):
    return render(request, 'accounts/apis_endpoint/subjects.html')

@login_required
def chatbot_view(request):
    return render(request, 'accounts/apis_endpoint/chatbot.html')

@login_required
def response_view(request):
    return render(request, 'accounts/apis_endpoint/response.html')

@login_required
def quiz_view(request):
    return render(request, 'accounts/apis_endpoint/quiz.html')


BASE_URL = "http://localhost:8000"

# Helper function to get a new token
def get_token():
    login_url = f"{BASE_URL}/api/v1/auth/login"
    payload = {'username': 'Superadmin', 'password': 'Password$404'}
    response = requests.post(login_url, json=payload)
    response_data = response.json()
    token = response_data.get('data', None)
    return token if response.status_code == 200 else None

# Function to call the /load_path/ endpoint
def test_load_path(course_id, student_id):
    url = f"{BASE_URL}/load_path/"
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "courseId": course_id,
        "studentId": student_id
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else None

# Django view to handle AJAX request
def load_path_view(request):
    if request.method == "POST":
        # Get course_id and student_id from POST data
        course_id = request.POST.get("courseId")
        student_id = request.POST.get("studentId")

        # Call the test_load_path function
        result = test_load_path(course_id, student_id)

        if result:
            return JsonResponse({"success": True, "data": result})
        else:
            return JsonResponse({"success": False, "error": "Failed to load course path"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

def query_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        query_text = data.get("query", "")

        base_url = "http://162.19.111.174:80"  # Replace with your actual base URL
        response = test_query_api(base_url, query_text)

        # Return the response as a JsonResponse
        if isinstance(response, dict):
            return JsonResponse(response, safe=False)
        else:
            # In case the response is not a dictionary, handle it as an error
            return JsonResponse({"error": "Invalid response from the API"}, status=500)


def test_query_api(base_url, query_text, optional_param=None):
    url = f"{base_url}/query/"
    payload = {
        "query": query_text
    }

    if optional_param:
        payload["optional_param"] = optional_param

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()  # Ensure the API response is in JSON format
        except ValueError:
            # Handle the case where the response is not valid JSON
            return {
                "error": "The API response is not valid JSON.",
                "status_code": response.status_code,
                "response_text": response.text
            }
    else:
        return {
            "error": "API Test Failed",
            "status_code": response.status_code,
            "response_text": response.text
        }
