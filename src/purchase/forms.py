from django.forms import ModelForm
from .models import purchase

class PurchaseForm(ModelForm):
    class Meta:
        model = purchase
        fields = ["period", "prefectures","municipalities","name1","name2","phone_number","email_address","arrival_date"]
