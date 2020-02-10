from django.db import models

# Create your models here.
class userrole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=200)

    def __str__(self):

        return self.role_name

class company_profile(models.Model):
    role_id = models.ForeignKey(userrole,on_delete=models.CASCADE)
    company_email = models.EmailField(primary_key=True,max_length=255)
    company_password = models.CharField(max_length=1000)
    company_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15, default="")
    website_url = models.CharField(max_length=255)
    password_updated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    profile_updated = models.BooleanField(default=False)


    def __str__(self):
        return self.company_email

class hr_profile(models.Model):
    role_id = models.ForeignKey(userrole, on_delete=models.CASCADE)
    hr_firstname = models.CharField(max_length=255)
    hr_lastname = models.CharField(max_length=255)
    hr_fullname = models.CharField(max_length=255, default="")
    hr_email = models.EmailField(max_length=255)
    hr_password = models.CharField(max_length=1000)
    hr_mobile = models.CharField(max_length=15, default="")
    hr_emp_id = models.CharField(
        max_length=1000, unique=True, primary_key=True, default="")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.hr_email



class emp_profile(models.Model):
    role_id = models.ForeignKey(userrole, on_delete=models.CASCADE)
    emp_firstname = models.CharField(max_length=255)
    emp_lastname = models.CharField(max_length=255)
    emp_fullname = models.CharField(max_length=255, default="")
    emp_email = models.EmailField(max_length=255, default="")
    emp_password = models.CharField(max_length=1000)
    emp_mobile = models.CharField(max_length=10,default="")
    emp_id = models.CharField(
        max_length=1000, primary_key=True, unique=True, default="")

    def __str__(self):
        return self.emp_email