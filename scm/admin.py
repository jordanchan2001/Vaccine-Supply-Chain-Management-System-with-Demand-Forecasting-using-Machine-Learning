from django.contrib import admin
from .models import Profile,Vaccine,Cart,CartItems,Shipment,SupplyChain

# Register your models here.
admin.site.register(Profile)
admin.site.register(Vaccine)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(SupplyChain)
admin.site.register(Shipment)