# health/views.py

from django.shortcuts import render, redirect
from .forms import SymptomForm
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, 'model')

model = joblib.load(os.path.join(MODEL_DIR, 'symptom_risk_model.joblib'))
label_encoder = joblib.load(os.path.join(MODEL_DIR, 'label_encoder.joblib'))
precaution_map = joblib.load(os.path.join(MODEL_DIR, 'precaution_map.joblib'))
severity_map = joblib.load(os.path.join(MODEL_DIR, 'severity_map.joblib'))

def diagnose(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['description']
            label = model.predict([desc])[0]
            disease = label_encoder.inverse_transform([label])[0]
            precautions = precaution_map.get(label, {})
            severity = severity_map.get(label, "Unknown")

            result = {
                'disease': disease,
                'severity': severity,
                'precautions': list(precautions.values())
            }

            return render(request, 'result.html', {'result': result})  # ✅

    else:
        form = SymptomForm()
    return render(request, 'input.html', {'form': form})  # ✅
