from django.contrib import admin

# Register your models here.
from payments.models import Paymentdetail
from django.contrib.admin.sites import site


class PaymentdetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_no',
                    'total_cost', 'payment_status', 'useremail', 'username', 'password')


admin.site.register( Paymentdetail,PaymentdetailAdmin)
