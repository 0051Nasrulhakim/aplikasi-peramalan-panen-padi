# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Prediction
import numpy as np
import joblib

model = joblib.load('datas/regression_model.joblib')

def index(request):
    return render(request, 'index.html')

def predict(request):
    tahun = int(request.POST.get('tahun'))
    prediction = model.predict(np.array([[tahun]]))[0]

    # Bulatkan nilai hasil prediksi menjadi angka bulat
    rounded_prediction = round(prediction)

    # Simpan hasil prediksi ke dalam database
    Prediction.objects.create(tahun=tahun, jumlah_produksi=rounded_prediction)

    context = {'result': rounded_prediction, 'tahun': tahun}
    return render(request, 'result.html', context)
