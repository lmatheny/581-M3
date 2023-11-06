from django.shortcuts import render 
from datetime import datetime
from django.http import HttpResponse
from .models import CalendarEntry  # Replace the dot with the appropriate app name
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'test' and password == 'pass':
            return render(request, 'base.html')  # Change 'base.html' to 'logo.html'
        else:
            return HttpResponse('Invalid credentials. Please try again.')
    else:
        return render(request, 'login.html')
    

def home_view(request):
    # opens html page
    return render(request, 'home.html')

def newDay_view(request):
     # opens html page
    if request.method == 'POST':
        return render(request, 'index.html')
    

    return render(request, 'newDay.html')

def stopwatch_view(request):
     # opens html page
    return render(request, 'stopwatch.html')


def calendar_view(request):
    # Query the database to get the calendar entries
    calendar_entries = CalendarEntry.objects.all()

    # Pass the entries to the template
    return render(request, 'calendar.html', {'calendar_entries': calendar_entries})


class CalendarEntryDetailView(DetailView):
    #creates new item for list
    model = CalendarEntry
    template_name = 'calendar_entry_detail.html'
    context_object_name = 'entry'


def edit_entry(request, entry_id):
    entry = get_object_or_404(CalendarEntry, pk=entry_id)
    
    if request.method == 'POST':
        # Get the edited data from the form
        new_date = request.POST.get('date')
        new_total_time = request.POST.get('total_time')
        
        # Update the CalendarEntry instance
        entry.date = new_date
        entry.total_time = new_total_time
        entry.save()
        
        return redirect('calendar-entry-detail', entry_id=entry.id)
    
    return render(request, 'edit_entry.html', {'entry': entry})



def person_view(request):
    # Fetch the user's profile data here
    username = "Lmatheny"
    email = "luke@gmail.com"
    password = "*****"

    if request.method == 'POST':
        # Handle POST request to update the profile here
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')

        context = {
        'username': new_username,
        'email': new_email,
        'password': new_password }


        # Perform the update operation here

        # Redirect to the profile page after the update
        return render(request, 'person.html',context)

    context = {
        'username': username,
        'email': email,
        'password': password,
    }

    return render(request, 'person.html', context)