from django.shortcuts import render

# Create your views here.
def services(request):
    context = {
    }

    return render (request, "services.html", context = context)