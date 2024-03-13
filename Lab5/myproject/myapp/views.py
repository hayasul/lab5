from django.shortcuts import render

# myapp/views.py
from django.shortcuts import render, redirect
from .models import Person

people = []

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username=username, password=password)
        person.save()
        people.append(person)
        return redirect('all_people')
    return render(request, 'add_person.html')

def all_people(request):
    context = {'people': people}
    return render(request, 'all_people.html', context)

