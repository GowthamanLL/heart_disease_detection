from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy as np
import joblib
import os
import joblib
import numpy as np
from django.shortcuts import render
from .forms import PricePredictionForm
import sklearn
from joblib import load
# Create your views here.
model=load('.\models\saved_model.joblib')
def index(request):
    return HttpResponse("hello world")
def index1(request):
   return render(request,'index.html')
def user(request):
    age=request.GET['age']
    anaemia = request.GET['anaemia']
    creatinine_phosphokinase = request.GET['creatinine_phosphokinase']
    diabetes= request.GET['diabetes']
    ejection_fraction = request.GET['ejection_fraction']
    high_blood_pressure = request.GET['high_blood_pressure']
    platelets = request.GET['platelets']
    serum_creatinine= request.GET['serum_creatinine']
    serum_sodium=request.GET['serum_sodium']
    sex	=request.GET['sex']
    smoking=request.GET['smoking']
    time=request.GET['time']
    y_pred=model.predict([[int(age),int(anaemia),int(creatinine_phosphokinase),int(diabetes),int(ejection_fraction),int(high_blood_pressure),float(platelets),int(serum_creatinine),int(serum_sodium),int(sex),int(smoking),int(time)]])
    # print(y_pred)
    # if y_pred==1:
    #     y_pred="The person has chance of Heart Failure"
    # if y_pred==0:
    #     y_pred="The person not have chance of Heart Failure"
    return render(request,'user.html',{'predict':y_pred})
        