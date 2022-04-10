from django.urls import path

from .views import ButtonClickCreateView

urlpatterns = [
    path('button_click/', ButtonClickCreateView.as_view()),
]
