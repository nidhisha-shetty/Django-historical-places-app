from django.shortcuts import render
from django.http import HttpResponse

		#Create your views here.

# def home_view(request, *args, **kwargs):						#similarlly we can use "def home_view(request):"
# 	print(args, kwargs)
# 	return HttpResponse("<H1> MY HISTORICAL PLACES PAGE</H1>") #requires "from django.http import HttpResponse"


def home_view(request):
	context={
		'text': "testing context",
		'number': "testing context"
	}
	return render(request, "home.html", context)

