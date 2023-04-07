from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pickle
import os
from django.http import JsonResponse


def index(request):
    if request.method == 'POST':
        model_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'Notebook/models/heart_pred.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        age = int(request.POST['age'])
        sex = int(request.POST['sex'])
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])
        prediction = model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        return render(request, 'result.html', {'prediction': prediction[0]})

    return render(request, 'heart.html')
