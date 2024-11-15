from django.urls import path
from .views import subjects_view,load_path_view, chatbot_view, query_api, response_view, quiz_view

urlpatterns = [
    path('', subjects_view, name='subjects'),
    path('api/load_path/', load_path_view, name='load_path_view'),
    path('chatbot/', chatbot_view, name='chatbot-view'),
    path('response/', response_view, name='response-view'),
    path('quiz/', quiz_view, name='quiz-view'),
    path('api/query/', query_api, name='query_api'),
]

