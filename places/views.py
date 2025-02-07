from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Places
from .forms import Form

		#Create your views here.

# def home_view(request, *args, **kwargs):						#similarlly we can use "def home_view(request):"
# 	print(args, kwargs)
# 	return HttpResponse("<H1> MY HISTORICAL PLACES PAGE</H1>") #requires "from django.http import HttpResponse"


def home_view(request):
	
	return render(request, "home.html")

def create_view(request):
	form = Form(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form=Form()
	context = {
		'form': form
	}
	return render(request, "create.html", context)


def edit_view(request, my_id):
	o=Places.objects.get(id=my_id)
	form=Form(request.POST or None, request.FILES or None, instance=o)
	if form.is_valid():
		form.save()
		form=Form()
	context={
	'form': form
	}
	return render(request, "edit.html", context)

def delete_view(request, my_id):
	o=Places.objects.get(id=my_id)
	if request.method=='POST':
		o.delete()
		return redirect("http://127.0.0.1:8000/")

	context={
	'object':o.place_name
	}
	return render(request, "delete.html", context)

def list_read_view(request):
	o=Places.objects.all()
	context = {
	'obj': o
	}
	return render(request, "list_read.html", context)

def read_view(request, my_id):
	o=Places.objects.get(id=my_id)
	context = {
	'obj': o
	}
	return render(request, "read.html", context)

def list_edit_view(request):
	o=Places.objects.all()
	context = {
	'obj': o
	}
	return render(request, "list_edit.html", context)

def list_delete_view(request):
	o=Places.objects.all()
	context = {
	'obj': o
	}
	return render(request, "list_delete.html", context)