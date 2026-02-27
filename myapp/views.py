from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว ✅")
        return redirect("form")

    return render(request, "form.html")