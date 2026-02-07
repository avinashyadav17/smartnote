from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('create/', views.create_note, name='create_note'),
    path('notes/', views.notes_list, name='notes_list'),
    path('update/<int:id>/', views.update_note, name='update_note'),
    path('delete/<int:id>/', views.delete_note, name='delete_note'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),

]
