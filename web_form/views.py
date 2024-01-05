from django.shortcuts import render, HttpResponseRedirect
from .models import user_form
from django.contrib import messages
from .forms import dj_form

# Create your views here.
def display_form(request):
    if request.method == "POST":
        data = dj_form(request.POST, request.FILES)
        if data.is_valid:
            data.save()
            messages.success(request, "Form Submitted Successfully...")

            a = user_form.objects.all()
            return HttpResponseRedirect('/form/')
    else:
        data = dj_form()
        return render(request, 'index.html', {'form':data})

def data_display(request):
    a = user_form.objects.all()
    return render(request, 'data.html', {'data':a})

def update(request):
    if request.method == "GET":
        id_user = request.get('')

