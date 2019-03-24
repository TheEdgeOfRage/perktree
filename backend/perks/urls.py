from django.urls import path
from perks import views

urlpatterns = [
	path('trees', views.Trees.as_view()),
	path('trees/<int:tree_id>', views.Perks.as_view()),
]

