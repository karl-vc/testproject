from django.shortcuts import render,HttpResponse
from testApp.models import *
from testApp.forms import *


# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:
            role = int(request.POST.get('role_id'))
            if int(role) == 1:
                if form.is_valid():
                    email = request.POST['email']
                    password = request.POST['password']

                    try:
                        company_data = company_profile.objects.get(company_email = email)

                        if email == company_data.company_email:#to check if email entered is same as the admin's/company's email
                            try:
                                #check if password is updated/decrypted
                                if not company_data.password_updated:
                                    if password == company_data.company_password:
                                        print(password)


                                        return HttpResponse('this is working')
                                        #return render(request,'all-project.html')
                                    elif password != company_data.company_password:
                                        return HttpResponse("invalid password")


                                if company_data.password_updated:
                                    print(password)
                                    return render(request,'all-project.html')


                            except:
                                return render(request,'login.html',{'invalid_credentials':True,'form':form})
                        else:
                            return HttpResponse('emails does not exist')


                    except:
                        return render(request,'login.html',{'invalid_credentials':True,'form':form})

                if not form.is_valid():
                    form = LoginForm(request.POST)
                    return render(request,'login.html',{'invalid_credentials':True,'form':form})



            else:
                form = LoginForm(request.POST)
                return render(request,'login.html',{'invalid_credentials': True,'form': form})

        except:
            form = LoginForm(request.POST)
            return render(request,'login.html',{'invalid_credentials':True,'form':form})

    return render(request,'login.html',{'invalid_credentials':True,'form':form})


def project(request):
    return render(request,'all-project.html')