from django.contrib import admin
from django.urls import include, path




#all links from the project URL file
urlpatterns = [
    path('CNIT581-048-Milestone3/', include('milestone3.urls')),
    path('newDay/', include('milestone3.urls')),
    path('person/', include('milestone3.urls')),
    path('stopwatch/', include('milestone3.urls')),
    path('calendar/', include('milestone3.urls')),
    path('home/', include('milestone3.urls')),
    path('admin/', admin.site.urls),
  
]
