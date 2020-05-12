from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(cards_info)
admin.site.register(user)
admin.site.register(customer)
admin.site.register(bankinfo)
admin.site.register(operator)
admin.site.register(attendant)
admin.site.register(cleaner)
admin.site.register(driver)
admin.site.register(rest_stop_contact)

