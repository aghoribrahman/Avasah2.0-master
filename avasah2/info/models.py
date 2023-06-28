from django.db import models
from django.utils import timezone

class Query_model(models.Model):  
    full_name = models.CharField(max_length=50)  
    phone_number  = models.CharField(max_length=12)
    email_id = models.EmailField()
    property_type = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    budget = models.IntegerField()
    other_info = models.TextField(max_length=300,default='None')
    reference = models.CharField(max_length=100,default='None')
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = 'Customer Query'

class Contact_model(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=13)
    email_id = models.EmailField()
    other_info = models.TextField(max_length=300,default='None')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contacts Data'

class Property_Category(models.Model):
    type_of_property = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Property_Categories'
    def __str__(self):
        return self.type_of_property


class property_infomation(models.Model):
    category = models.ForeignKey(Property_Category,on_delete=models.CASCADE)
    property_name = models.CharField(max_length=100)
    property_timeline  = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    rera_number = models.CharField(max_length=100)
    property_detail = models.TextField()
    youtube_link = models.CharField(max_length=200)
    amenities = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.property_name

class Image(models.Model):
    image_name = models.ForeignKey(property_infomation,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

class Property_Table(models.Model):  
    Area = models.CharField(max_length=100)  
    Property_Type  = models.CharField(max_length=100)
    Property_Size = models.CharField(max_length=100)  
    Rate = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Area
    