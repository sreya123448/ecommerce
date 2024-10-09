from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def View_SuperAdmin(request):
    view=User.objects.all()
    print(view)
    return render(request,'superadmin_view.html',{'view':view})


def Create_SuperAdmin(request):
    if request.method=='POST':
        print(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email") 
        Screate = User.objects.create_user(username=username,email=email)
        Screate.save()
        print(Screate)
        return redirect('superadmin_view')
    return render(request,'superadmin_create.html')

def delete(request,id):
    a = User.objects.get(pk=id)
    a.delete()
    return redirect('superadmin_view')

def SuperAdmin_Edit(request,id):
    data=User.objects.get(id=id)

    if request.method == "POST":
        data.username = request.POST['username']
        data.email = request.POST['email']
        data.save()

        return redirect('superadmin_view')
    return render(request,'superadmin_edit.html',{'a':data})    