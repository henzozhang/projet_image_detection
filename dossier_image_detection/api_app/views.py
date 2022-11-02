from django.shortcuts import render

# Create your views here.
from urllib import response
from django.shortcuts import render
from . import forms
import json
from dotenv import load_dotenv
import os
import requests
from django.contrib.auth.decorators import login_required

load_dotenv()


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')



@login_required
def api(request):
    print(CLIENT_ID)
    print(CLIENT_SECRET)


    url_api="https://api.everypixel.com/v1/faces"

    if request.method =="POST":
            form = forms.ApiForm(request.POST)
            if form.is_valid():
                # param = {"url": form.url, "num_keywords":form.num_keywords}
                print(form.cleaned_data)
                reponse = requests.get(url_api, params = form.cleaned_data, auth =(CLIENT_ID,CLIENT_SECRET))
                form.save()
                info = json.loads(reponse.text)["faces"]
                print(info)
                print(form.cleaned_data)
                return render(request, 'api_app/reponse_formulaire.html', context = {'form' : form, 'info':info, 'nombre_personne': len(info), 'url':form.cleaned_data['url']})

    else :
        form = forms.ApiForm()
    return render(request, 'api_app/formulaire.html', context = {'form' : form})
    print(CLIENT_SECRET)
