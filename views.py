#from django.shortcuts import render
from mango.apple import render
from django.http import HttpResponse
from .models import *
# Create your views here.

# def func(request):

    # a = Abhi(name = "abhi01",address = "pune",empID = 100)
    # a.save()
#     return HttpResponse(request,".html", context={})


# def func1(request):

#     return render(request,".html",context={})

# def TAM(request):
#     if request.method=='POST':
#         Name=request.POST.get("nm")
#         Address=request.POST.get("add")
#         City=request.POST.get("city" )
#         Pincode=request.POST.get("pin")
#         ar= Aru(Name,Address,City,Pincode)
#         ar.save()
#         print(Name,Address,City,Pincode)
#     else:
#            return HttpResponse(request,".html", context={})

#     return HttpResponse("printed on control please check:")



def abhi(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        empID = request.POST.get("empID")
        sid = request.POST.get("staffid")
        a = PAM(name,address,empID,sid)
        a.save()
        print(name)
        print(address)
        print(empID)
        print(sid)
    else:
        return render(request,"page1.html",context={})
    return HttpResponse("printed on Console, please Check!!")