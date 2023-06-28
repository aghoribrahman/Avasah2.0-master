from django.contrib import admin
from .models import Query_model, Contact_model, property_infomation, Image,Property_Category,Property_Table

@admin.register(Query_model)
class Query_model_admin(admin.ModelAdmin):
    list_display =["created_at","full_name","phone_number","email_id","property_type","area","budget","other_info",]

@admin.register(Contact_model)
class Contact_model_admin(admin.ModelAdmin):
    list_display =["created_at","full_name","phone_number","email_id",]

@admin.register(property_infomation)
class property_infomations_admin(admin.ModelAdmin):
    list_display =["id","category","property_name","property_timeline","property_type","status","rera_number","property_detail","youtube_link","amenities"]

@admin.register(Image)
class property_infomations_admin(admin.ModelAdmin):
    list_display =["id","image_name","image"]

@admin.register(Property_Category)
class property_infomations_admin(admin.ModelAdmin):
    list_display =["id","type_of_property"]

@admin.register(Property_Table)
class Property_Table_admin(admin.ModelAdmin):
    list_display =["Area","Property_Type","Property_Size","Rate"]