from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_player/', views.add_player, name='add_player'),
    path('list_players/', views.list_players, name='list_players'),
    path('logout/', views.logout_view, name='logout'),
    path('notices/', views.notice_list, name='notice_list'),
    path('notices/create/', views.create_notice, name='create_notice'),
    path('notices/approve/', views.approve_notices, name='approve_notices'),
    path('notices/approve/<int:notice_id>/', views.approve_notice, name='approve_notice'),
    path('schedule/', views.event_schedule, name='event_schedule'),
    path('schedule/create/', views.create_event, name='create_event'),
    path('standings/', views.standings, name='standings'),
    path('match/create/', views.create_match, name='create_match'),
]