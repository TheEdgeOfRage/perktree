from django.urls import path
from perks import views

urlpatterns = [
	path('trees', views.ListTrees.as_view()),
	path('trees/<int:tree>', views.ListPerks.as_view()),
]

