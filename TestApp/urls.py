from django.urls import path
from TestApp import views

app_name='webclass'
urlpatterns = [
    path('Team/',views.Team,name="Team"),
    path('delete_Team/<int:id>',views.delete_Team,name="delete_Team"),

    path('Player_Category/',views.Player_Category,name="Player_Category"),
    path('delete_Player_Category/<int:id>',views.delete_Player_Category,name="delete_Player_Category"),

    path('Player_Detail/',views.Player_Detail,name="Player_Detail"),
    path('delete_Player_Detail/<int:id>',views.delete_Player_Detail,name="delete_Player_Detail"),



]


