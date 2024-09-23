from django import forms

class PricePredictionForm(forms.Form):
    age = forms.FloatField(label='age', min_value=0.0)
    anaemia = forms.IntegerField(label='anaemia', min_value=0)
    creatinine_phosphokinase = forms.IntegerField(label='creatinine_phosphokinase', min_value=0)
    diabetes= forms.IntegerField(label='diabetes', min_value=0)
    ejection_fraction = forms.IntegerField(label='ejection_fraction', min_value=0)
    high_blood_pressure = forms.IntegerField(label='high_blood_pressure')
    platelets = forms.FloatField(label='platelets', min_value=0.0)
    serum_creatinine= forms.FloatField(label='serum_creatinine', min_value=1.0)
    serum_sodium=forms.IntegerField(label='serum_sodium', min_value=0)
    sex	=forms.IntegerField(label='sex', min_value=0)
    smoking=forms.IntegerField(label='smoking', min_value=0)
    time=forms.IntegerField(label='time', min_value=0)	