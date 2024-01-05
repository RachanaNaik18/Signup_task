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
            return HttpResponseRedirect('/form/')
    else:
        data = dj_form()
        return render(request, 'index.html', {'form':data})

def data_display(request):
    a = user_form.objects.all()
    return render(request, 'data.html', {'data':a})

def update(request, id):
    if request.method == "POST":
        id_user = user_form.objects.get(pk = id)
        id_form = dj_form(request.POST, instance=id_user)
        if id_form.is_valid:
            id_form.save()
            messages.success(request, "Data Updated Successfully...")
            return HttpResponseRedirect('/data/')
    else:
        id_user = user_form.objects.get(pk = id)
        id_form = dj_form(request.POST, instance=id_user)
    return render(request, "update.html", {'form': id_form})

def delete(request, id):
    if request.method == "GET":
        id_user = user_form.objects.get(pk = id)
        id_user.delete()
        return HttpResponseRedirect('/data/')





