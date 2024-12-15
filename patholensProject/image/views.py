from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from image.models import Diagnosis
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json

# Create your views here.
def diagnosisView(request):
    return render(request, 'diagnosisPage.html')


def diagnosisView(request, diagID): 
    diagnosisObj = Diagnosis.objects.get(diagID=diagID)
    return render(request, 'image/diagnosisPage.html', {'diagID': diagnosisObj.diagID})




@login_required
def newDiagnosis(request, diagnosisID):

    return render(request, "image/diagnosisPage.html", {"diagnosisID": diagnosisID})
