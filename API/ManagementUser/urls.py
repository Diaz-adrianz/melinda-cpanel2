from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListUser.as_view()),
    path('<int:pk>/delete/',views.destroyUser.as_view())
]
