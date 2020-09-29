from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import Sum

from .models import Fund, Commitment, Call, Drawdown

class FundAdmin(admin.ModelAdmin):
    list_display=[
        "id",
        "name",
       
        
    ]
    list_display_links=[
        "id",
        "name",

    ]


class CommitmentAdmin(admin.ModelAdmin):
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


    

class DrawdownAdmin(admin.ModelAdmin):

    # def get_call(self,obj):
    #     return obj.call.amount

    list_display=[
        "id",
        "call",
        "commitment",
        "date",
        "amount",
    ]
    
    

    list_display_links=[
        "id",
        "call",
    ]




class CallAdmin(admin.ModelAdmin):


    def allocated(self,obj):
        total=Drawdown.objects.filter(call=obj).aggregate(Sum("amount"))
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
admin.site.register(Commitment,CommitmentAdmin)
admin.site.register(Call,CallAdmin)
admin.site.register(Drawdown,DrawdownAdmin)

admin.site.unregister(Group)



