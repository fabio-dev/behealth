from django.shortcuts import render
#from django.http import HttpResponseRedirect, HttpResponse
#from django.template import loader
from .forms import BMIForm, EERForm
from calculation import calculMethods
from datalayer import calculConst


def BMIFormView(request):
    result = 0
    if request.method == 'POST':
        form = BMIForm(request.POST)
        
        if form.is_valid():
            weight = form.cleaned_data['weight']
            size = form.cleaned_data['size']
            result = calculMethods.calculBMI(weight, size)
    else:
        form = BMIForm()
        
    return render(request, 'bmi/bmi.html', {'form': form, 'result': result})


def EERFormView(request):
    result = 0

    if request.method == 'POST':
        form = EERForm(request.POST)
        
        if form.is_valid():
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            size = form.cleaned_data['size']
            sex = form.cleaned_data['sex']
            activity = form.cleaned_data['activity']

            result = calculMethods.calculEER(age, weight, size, sex, activity)
            
    else:
        form = EERForm()

    return render(request, 'eer/eer.html', {'form': form, 'result': result })