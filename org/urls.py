from django.urls import path

from .views import WorkerView, PositionView

app_name = "workers"

urlpatterns = [
    path('workers/', WorkerView.as_view()),
    path('positions/', PositionView.as_view()),
]