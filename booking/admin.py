from django.contrib import admin

# Register your models here.
from .models import booking,transaction,passenger


admin.site.register(booking)
admin.site.register(transaction)
admin.site.register(passenger)