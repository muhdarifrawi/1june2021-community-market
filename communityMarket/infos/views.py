from django.shortcuts import render, HttpResponse

def main(request):
    return render(request,"infos/main.html")

def form_page(request):
    return render(request,"infos/submit.html")