from django.urls import path
from . import views

app_name = 'prediction'

urlpatterns = [
    path('API/', views.PredictView.as_view(), name='prediction'),
]