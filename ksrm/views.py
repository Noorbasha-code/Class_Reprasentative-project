from django.shortcuts import render,redirect
from .forms import Studentform
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
from .models import Student1

# Create your views here.
...



def submit(request):
	if request.method=='POST':
		data=Studentform(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse("<h1>alert('Data save succesfull.</h1>')")


		data=request.POST

		return HttpResponse('WELCOME TO'+ data['name'])
	stuform=Studentform()
	return render(request,'ksrm/submit.html',{'formfields':stuform})


def display(request):
	data=Student1.objects.all()
	return render(request,'ksrm/display.html',{'data':data})	

def view(request,id):
	data=Student1.objects.get(id=id)
	return render(request,"ksrm/view.html" ,{'data':data})


def delete(request,id):
	data=Student1.objects.get(id=id)
	if request.method == 'POST':
		data.delete()
		return redirect('/display')
	return render(request,"ksrm/delete.html",{'data':data})

def update(request,id):
	data = Student1.objects.get(id=id)
	form = Studentform(instance=data)
	if request.method=='POST':
		form = Studentform(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/display')
	return render(request,'ksrm/update.html',{'form':form})


def index(request):
		return render(request,'ksrm/index.html',{})

def download(request):
	return render(request,'ksrm/download.html',{})



def show(request):
	
	data=Log.objects.all()
	return render(request,'ksrm/show.html',{'data':data})


def save(request):
	if request.method=='POST':
		data=Collegeform(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse("<h1>Data save succesfull.</h1>")

		data=request.POST

		return HttpResponse('WELCOME TO'+ data['name'])
	clgform=Collegeform()
	return render(request,'ksrm/save.html',{'clgform':clgform})


def welcome(request):
	return render(request,'ksrm/hello.html',{})



