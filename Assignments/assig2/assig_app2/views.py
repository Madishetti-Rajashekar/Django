from django.shortcuts import render

# Create your views here.
def showInfo(request):
    num1 = request.POST.get("num1")
    num2 = request.POST.get("num2")
    add = request.POST.get("add")
    sub = request.POST.get("sub")
    mul = request.POST.get("mul")
    div = request.POST.get("div")
    if add :
        return render(request,'one.html',{"result":num1+num2})
    else:
        return render(request,'one.html')
