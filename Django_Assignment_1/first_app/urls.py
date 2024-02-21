from django.urls import path,include
from.import views
urlpatterns = [
    path('meals/',views.meals),
    path('sohan/',views.meal_view)
]
