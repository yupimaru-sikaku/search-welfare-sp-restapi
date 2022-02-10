from django.db import models

class Company(models.Model):

    def __str__(self):
        return str(self.id) + " - " + self.companyName

    companyName = models.CharField(unique= True, max_length = 50)
    companyNumber = models.CharField(unique= True, max_length = 13)
    postalCode = models.CharField(max_length = 7)
    address = models.CharField(max_length = 100)
    telephoneNumber = models.CharField(max_length = 11)
    faxNumber = models.CharField(blank=True, null=True,  max_length = 11)
    email = models.EmailField(max_length = 100)
    humanName = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add=True)

class Office(models.Model):

    def __str__(self):
        return str(self.id) + " - " + self.officeName

    target_company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    officeName = models.CharField(unique= True, max_length = 50)
    postalCode = models.CharField(max_length = 7)
    address = models.CharField(max_length = 100)
    telephoneNumber = models.CharField(max_length = 11)
    faxNumber = models.CharField(blank=True, null=True,  max_length = 11)
    email = models.EmailField(max_length = 100)
    humanName = models.CharField(max_length = 10)
    capacity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
