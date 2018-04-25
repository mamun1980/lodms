from django.shortcuts import render

# Create your views here.

def casems_home(request):
	# return HttpResponse('hello world!')
	return render(request, 'casems_home.html', {})