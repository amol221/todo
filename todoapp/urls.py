from django.urls import path
from . import views

urlpatterns =[
    path('addTask/',views.addTask , name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done,name = 'mark_as_done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone,name = 'mark_as_undone'),

    # DELETE
    path('delete_tasks/<int:pk>/',views.delete_tasks,name='delete_tasks'),

    #EDIT
    path('update_tasks/<int:pk>/',views.update_tasks,name='update_tasks'),

]