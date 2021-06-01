from django.shortcuts import render, HttpResponse

def main(request):
    return render(request,"infos/main.html")
