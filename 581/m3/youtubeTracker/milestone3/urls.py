from django.urls import path
from . import views
from .views import CalendarEntryDetailView


#links to all pages
urlpatterns = [
    path('', views.index, name='index'),
    path('person.html', views.person_view, name='person'),
    path('index.html', views.home_view, name='person'),
     path('stopwatch.html', views.stopwatch_view, name='stopwatch'),
    path('calendar.html', views.calendar_view, name='calendar_view'),
    path('newDay.html', views.newDay_view, name='newDay'),
     path('home.html', views.home_view, name='home'),
    path('calendar_entry/edit/<int:entry_id>/', views.edit_entry, name='edit-calendar-entry'),
    path('calendar_entry/<int:pk>/', CalendarEntryDetailView.as_view(), name='calendar-entry-detail'),
]