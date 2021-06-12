from django.shortcuts import render

# Create your views here.
def displayInfo(request):
    user_name=request.POST.get('username')
    pass_word=request.POST.get('password')
    type=request.POST.get('type')
    if (user_name == 'Ravi') and (pass_word in ["ravi1234@","kumar@123","ravikumar@123"]):
        if type=='Admin' and pass_word=="ravi1234@":
            return render(request,'welcome.html',{'message':'Admin'})
        elif type=='Employee' and pass_word=="kumar@123":
            return render(request,"welcome.html",{'message':'Employee'})
        elif type=="Customer" and pass_word=="ravikumar@123":
            return render(request,"welcome.html",{'message':'Customer'})
        else:
            return render(request,'welcome.html')
    else:
        return render(request,"index.html",)





