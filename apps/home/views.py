
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from apps.home.models import Log


@login_required(login_url="/login/")
def index(request):
    logs = Log.objects.all()
    return render(request, "home/dashboard.html", {"logs": logs})


@csrf_exempt
def insertLog(request):
    if request.method == "POST":
        plate = request.POST.get("plate", None)
        kms = request.POST.get("kms", None)
        comb = request.POST.get("comb", None)

        if kms is not None and comb is not None:
            Log(matricula=plate, kms=kms, comb=comb).save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(f"plate = {plate}, kms = {kms}, comb = {comb}", status=415)

    else:
        return HttpResponse("DSA", status=400)
