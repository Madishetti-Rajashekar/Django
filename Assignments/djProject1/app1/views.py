from django.shortcuts import render

# Create your views here.
def displayInfo(request):
    return render(request,'one.html')

def showInfo(request):
    name=request.POST.get("user_name")
    password=request.POST.get("passwrd")
    if name=='Rajashekar' and password=='@Raju1995@':
        return render(request,'two.html')
    else:
        return render(request,'three.html')