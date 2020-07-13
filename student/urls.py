from django.urls import path
from .views import *


urlpatterns = [
    path('create', create_student, name='create-student'),
    path('result', get_result, name='get-result'),
]