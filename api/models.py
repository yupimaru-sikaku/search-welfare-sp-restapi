from django.db import models

class Company(models.Model):

    companyName = models.CharField(unique= True, max_length = 50)
    companyNumber = models.CharField(unique= True, max_length = 13)
    postalCode = models.CharField(max_length = 7)
    address = models.CharField(max_length = 100)
    telephoneNumber = models.CharField(max_length = 11)
    faxNumber = models.CharField(blank=True, null=True,  max_length = 11)
    email = models.EmailField(max_length = 100)
    humanName = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.companyName

class Office(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    officeName = models.CharField(unique= True, max_length = 50)
    postalCode = models.CharField(max_length = 7)
    address = models.CharField(max_length = 100)
    telephoneNumber = models.CharField(max_length = 11)
    faxNumber = models.CharField(blank=True, null=True,  max_length = 11)
    email = models.EmailField(max_length = 100)
    humanName = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.officeName

class Service(models.Model):

    STATUS_DEFAULT = "共同生活援助（介護サービス包括型）"
    STATUS_SET = (
            ("共同生活援助（介護サービス包括型）", "共同生活援助（介護サービス包括型）"),
            ("就労継続支援B型", "就労継続支援B型"),
            ("生活介護", "生活介護"),
            ("計画相談支援", "計画相談支援"),
            ("重度訪問介護", "重度訪問介護"),
            ("児童発達支援", "児童発達支援"),
            ("障がい児相談支援", "障がい児相談支援"),
    )

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    officeNumber = models.CharField(unique= True, max_length = 11)
    serviceType = models.CharField(choices=STATUS_SET, default=STATUS_DEFAULT, max_length=50)
    capacity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.serviceType