from django.contrib import admin

# Register your models here.
from payments.models import Paymentdetail
from django.contrib.admin.sites import site


class PaymentdetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'order_no',
                    'total_cost', 'payment_status', 'useremail')


admin.site.register(Paymentdetail, PaymentdetailAdmin)
