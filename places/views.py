from django.shortcuts import render
from django.http import HttpResponse
from .models import Places
from .forms import Form

		#Create your views here.

# def home_view(request, *args, **kwargs):						#similarlly we can use "def home_view(request):"
# 	print(args, kwargs)
# 	return HttpResponse("<H1> MY HISTORICAL PLACES PAGE</H1>") #requires "from django.http import HttpResponse"


def home_view(request):
	o=Places.objects.get(id=5)
	context={
		'obj':o.place_image
	}
	return render(request, "home.html", context)

def create_view(request):
	form = Form(request.POST or None)
	if form.is_valid():
		form.save()
		form=Form()
	context = {
		'form': form
	}
	return render(request, "create.html", context)

def edit_view(request):
	o=Places.objects.get(id=10)
	form=Form(request.POST or None, request.FILES or None, instance=o)
	if form.is_valid():
		form.save()
	context={
	'form': form
	}
	return render(request, "edit.html", context)
