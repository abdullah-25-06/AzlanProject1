from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.urls import reverse


#
# Create your views here.
def index(request):
    return HttpResponse("Working")


class Forms(View):
    def get(self, request):
        return render(request, 'Sis/Formdisp1.html', {
            'form': StudentForm()
        })

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been register')
            return HttpResponseRedirect(reverse('sis:list'))
        else:
            return render(request, 'Sis/Formdisp1.html', {
                'form': form
            })


def Formlist(request):
    lists = Student.objects.all()
    return render(request, 'Sis/Formlist.html', {
        'list': lists
    })


def detail(request, id):
    details = Student.objects.get(pk=id)
    return render(request, 'Sis/Formdetail.html', {
        'detail': details
    })
