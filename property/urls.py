from django.urls import path
from .views import PropertyList, PropertyDetails

urlpatterns = [
    # path('', views.index),
    path('', PropertyList.as_view()),
    path('<int:property_auto>', PropertyDetails.as_view()),
]
