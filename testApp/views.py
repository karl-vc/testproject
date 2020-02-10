from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render,HttpResponse, redirect
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
                                        request.session['user_email'] = email
                                        request.session['user_role_id'] = company_data.role_id_id
                                        request.session['user_is_authenicated'] = True

                                        #link page for updation of password
                                        return render(request, 'change-password.html')



                                    elif password != company_data.company_password:
                                        return render(request, 'login.html', {'invalid_cred': True, 'form': form})
                                        # return HttpResponse("invalid password")


                                if company_data.password_updated:
                                    if password == company_data.company_password:
                                        request.session['user_email'] = email
                                        request.session['user_role_id'] = company_data.role_id_id
                                        request.session['user_is_authenticated'] = True

                                        return redirect('/dash/')

                                    # if check_password(password,company_data.company_userpassword):
                                    #     return render(request, 'all-project.html')
                                    #     if not company_data.profile_updated:
                                    #         # return HttpResponse('profile is not encrypted so do something to make it encrypteed')
                                    #         return render(request, 'all-project.html')
                                    #     if company_data.profile_updated:
                                    #         return render(request, 'all-project.html')
                                    # else:
                                    #     return render(request,'all-project.html')



                            except:
                                return render(request,'login.html',{'invalid_cred':True,'form':form})
                        else:
                            return render(request, 'login.html', {'invalid_cred': True, 'form': form})
                            # return HttpResponse('emails does not exist')


                    except:
                        return render(request,'login.html',{'invalid_cred':True,'form':form})

                if not form.is_valid():
                    form = LoginForm(request.POST)
                    return render(request,'login.html',{'invalid_cred':True,'form':form})

            elif int(role) == 2:
                if form.is_valid:
                    email=request.POST['email']
                    password = request.POST['password']
                    hr_data = hr_profile.objects.get(hr_email = email)

                    if password == hr_data.hr_password:
                        request.session['user_email'] = email
                        request.session['user_role_id'] = hr_data.role_id_id
                        request.session['user_is_authenticated'] = True
                        return redirect('/dash/')
                    else:
                        form = LoginForm(request.POST)
                        return render(request,'login.html',{'invalid_cred':True,'form':form})



                elif not form.is_valid:
                    form = LoginForm(request.POST)
                    return render(request, 'login.html', {'invalid_cred': True, 'form': form})

                # else:
                #     form = LoginForm(request.POST)
                #     return render(request,'login.html',{'invalid_cred': True,'form': form})
            elif int(role) == 3:
                if form.is_valid:
                    email= request.POST['email']
                    password =request.POST['password']
                    emp_data= emp_profile.objects.get(emp_email = email)
                    if password == emp_data.emp_password:
                        request.session['user_email'] = email
                        request.session['user_role_id'] = emp_data.role_id_id
                        request.session['user_is_authenticated'] = True

                        return redirect('/emp_dash/')
                    else:
                        return render(request,'login.html',{'invalid_cred':True,'form':form})
                elif not form.is_valid:
                    return render(request,'login.html',{'invalid_cred':True,'form':form})

            else:
                form = LoginForm(request.POST)
                return render(request,'login.html',{'invaliud_cred':True,'form':form})
        except:
            form = LoginForm(request.POST)
            return render(request,'login.html',{'invalid_cred':True,'form':form})

    return render(request,'login.html',{'invalid_cred':True,'form':form})

#dummy function
def project(request):
    return render(request,'all-project.html')


#function to change or update password
def change_pass(request):
    try:
        permission = request.session['user_is_authenticated']
    except:
        permission = False
    if permission:
        form = change_passForm()
        if request.session['user_role_id'] == 1:
            email = request.session['user_email']
            company_data = company_profile.objects.get(company_email = email)
            if company_data.password_updated:
                #if company/admin profile is updated
                if request.method == 'POST':

                    old_pass = request.POST['old_pass']
                    if old_pass == company_data.company_password:
                        new_pass = request.POST['new_pass']
                        confirm_pass = request.POST['confirm_pass']
                        if new_pass == confirm_pass:
                            encrypt_pass = make_password(confirm_pass)
                            update_pass = company_profile(company_email = email,company_password = encrypt_pass,password_updated = True)

                            update_pass.save(update_fields=['company_password','profile_updated'])

                            return render(request,'change-password.html',{'form':form,'password_updated':True, 'company_updated':company_data.profile_updated})

                        elif new_pass != confirm_pass:
                            return render(request,'change-passeword.html',{'pass_dont_match':True,'form':form})
                    elif old_pass != company_data.company_password:
                        return render(request,'change_password.html',{'invalid_pass':True,'form':form})

                return render(request,'change-passsword.html',{'form':form})

            #if company/admin profile is not updated


            elif not company_data.password_updated:
                if request.method == 'POST':

                    old_pass = request.POST('old_pass')
                    if old_pass == company_data.company_password:
                        new_pass = request.POST('new_pass')
                        confirm_pass = request.POST('confirm_pass')

                        if new_pass == confirm_pass:
                            encrypt_pass = make_password(confirm_pass)
                            update_pass = company_profile(company_password = encrypt_pass,company_email = email,password_updated = True)
                            update_pass.save(update_fields = ['company_password','profile_updated'])

                            return render(request,'change-password.html',{'form':form,'password_updated':True,'company_updated':company_data.profile_updated})

                        elif new_pass != confirm_pass:
                            return render(request, 'change-passeword.html', {'pass_dont_match': True, 'form': form})
                    elif old_pass != company_data.company_password:
                        return render(request, 'change_password.html', {'invalid_pass': True, 'form': form})

                return render(request,'change-password.html',{'form':form})


        #when login as HR
        elif request.session['user_role_id'] == 2:

            if request.method == 'POST':
                email = request.session['user_email']
                hr_data = hr_profile.objects.get(hr_email=email)

                old_pass=request.POST['old_pass']

                if old_pass == hr_data.hr_password:
                    new_pass = request.POST['new_pass']
                    confirm_pass = request.POST['confirm_pass']

                    if new_pass == confirm_pass:
                        encrypt_pass = make_password(confirm_pass)
                        update_pass = hr_profile(hr_emp_id =  hr_data.hr_emp_id, hr_password = encrypt_pass)

                        update_pass.save(update_fields=['hr_password'])

                        return render(request,'change-password.html',{'form':form,'password_updated':True})

                    elif new_pass != confirm_pass:
                        return render(request,'change-password.html',{'pass_dont_match':True,'form':form})
                elif old_pass != hr_data.hr_password:
                    return render(request,'change-password.html',{'form':form,'invalid_pass':True})

            return render(request,'change-password.html',{'form':form})

        #when login as employee

        elif request.session['user_role_id'] == 3:
            if request.method == 'POST':
                email= request.session['user_email']
                old_pass = request.POST['old_pass']
                emp_data = emp_profile.objects.get(emp_email = email)
                if old_pass == emp_data.emp_password:
                    new_pass = request.POST['new_pass']
                    confirm_pass = request.POST['confirm_pass']
                    if new_pass == confirm_pass:
                        encrypt_pass = make_password(confirm_pass)
                        update_pass = emp_profile(emp_password = encrypt_pass, emp_id = emp_data.emp_id)
                        update_pass.save(update_fields='emp_password')

                        return render(request,'change-password.html',{'form':form,'password_updated':True})
                    elif new_pass != confirm_pass:
                        return render(request,'change-password.html',{'form':form,'pass_dont_match':True})
                elif old_pass != emp_data.emp_password:
                    return render(request,'change-password.html',{'form':form,'invalid_pass':True})

            return render(request,'change-password.html',{'form':form})


    elif not permission:
        return HttpResponse('permission denied')


    return render(request,'change-password.html')

#combined dashboard for admin and HR staff
def dashboard(request):


    return render(request,'dashboard.html')


#main dashboard for employee staff
def emp_dash(request):

    return render(request,'employee-dashboard.html')