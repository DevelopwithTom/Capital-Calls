from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import Sum

from .models import Fund, Deposit, Call, Commitment

class FundAdmin(admin.ModelAdmin):
    list_display=[
        "id",
        "name",
       
        
    ]
    list_display_links=[
        "id",
        "name",

    ]


class DepositAdmin(admin.ModelAdmin):
    list_display=[
        "id",
        "fund",
        "date",
        "amount",
        "undrawn",
    ]
    list_display_links=[
        "id",
        "fund",
    ]


    

class CommitmentAdmin(admin.ModelAdmin):

    # def get_call(self,obj):
    #     return obj.call.amount

    list_display=[
        "id",
        "call",
        "deposit",
        "date",
        "amount",
    ]
    
    

    list_display_links=[
        "id",
        "call",
    ]




class CallAdmin(admin.ModelAdmin):


    def allocated(self,obj):
        total=Commitment.objects.filter(call=obj).aggregate(Sum("amount"))
        return total['amount__sum']


    list_display=[
        "id",
        "date",
        "amount",
        "allocated",
        
    ]
    list_display_links=[
        "id",
        "amount",

    ]


# Register your models here.
admin.site.site_header = 'Capital Calls Administration'


admin.site.register(Fund,FundAdmin)
admin.site.register(Deposit,DepositAdmin)
admin.site.register(Call,CallAdmin)
admin.site.register(Commitment,CommitmentAdmin)

admin.site.unregister(Group)



