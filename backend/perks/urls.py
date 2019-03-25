from django.urls import path
from perks import views

urlpatterns = [
	path('trees', views.TreeView.as_view()),
	path('trees/<int:tree_id>', views.PerkView.as_view()),
	path('users/<int:user_id>', views.UserView.as_view()),
]

