from django.shortcuts import render

# Create your views here.

def home_base(request):
	return render(request, 'home1.html',{'name':'priyal'})

def addition(request):
	val1 =int(request.POST['no1'])
	val2 =int(request.POST['no2'])
	additio = val1 + val2
	return render(request, 'result1.html',{'number': additio})
