from django.shortcuts import render
from django.http import HttpResponse
from .models import Places

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

