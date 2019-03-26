from django.urls import path
from perks import views

urlpatterns = [
	path('trees', views.TreeView.as_view()),
	path('trees/<int:tree_id>', views.PerkView.as_view()),
	path('user', views.UserView.as_view()),
	#  path('unlock/<int:perk_id>', views.UserView.as_view()),
]

