from django.contrib import admin
from django.db import models
from django.forms import ModelChoiceField

# Register your models here.
from nlmkapp.models import *

#admin.site.register(ObjectNLMK)

@admin.register(ObjectNLMK)
class ObjectNLMKAdmin(admin.ModelAdmin):
    list_display = ['objectnlmk', 'bgp_as', 'enterprise', 'enterprise_addr']
    search_fields = ('objectnlmk', 'bgp_as', 'enterprise', 'enterprise_addr',)

#admin.site.register(Operator)
@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ['operator', 'operator_name']
    search_fields = ('operator', 'operator_name',)

#admin.site.register(Channel)
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['ip', 'router', 'get_bgp_as', 'bandwidth']
    search_fields = ('ip', 'router', 'bgp_as__bgp_as')
        
    def get_bgp_as(self, obj):
        return obj.bgp_as.bgp_as
    
    get_bgp_as.short_description = "BGP AS"

#admin.site.register(Peering)
@admin.register(Peering)
class PeeringAdmin(admin.ModelAdmin):
    list_display = ['operator', 'contract']
    search_fields = ('operator',)

#admin.site.register(Type_channel)
@admin.register(Type_channel)
class Type_channelAdmin(admin.ModelAdmin):
    list_display = ['operator', 'type_channel']
    search_fields = ('operator__operator_name', 'type_channel',)
   
#admin.site.register(L3net) 
@admin.register(L3net)
class L3netAdmin(admin.ModelAdmin):
    list_display = ['operator', 'op_ip', 'our_ip']
    search_fields = ('op_ip', 'our_ip',)
	
#admin.site.register(Optelephone)
@admin.register(Optelephone)
class OptelephoneAdmin(admin.ModelAdmin):
    list_display = ['operator', 'telephone']
    search_fields = ('operator__operator_name','telephone',)
 
#admin.site.register(Opemail) 
@admin.register(Opemail)
class OpemailAdmin(admin.ModelAdmin):
    list_display = ['operator', 'email'] 
    search_fields = ('operator__operator_name', 'email',)
   
#admin.site.register(Voipgw)
@admin.register(Voipgw)
class VoipgwAdmin(admin.ModelAdmin):
    list_display = ['voip_ip', 'voip_gw'] 
    search_fields = ('voip_ip', 'voip_gw',)
    
#admin.site.register(Voipprefix)
@admin.register(Voipprefix)
class VoipprefixAdmin(admin.ModelAdmin):
    list_display = ['prefix', 'voipgw']
    search_fields = ('prefix', 'voipgw__voip_gw',)

#admin.site.register(Clientcontact)
@admin.register(Clientcontact)
class ClientcontactAdmin(admin.ModelAdmin):
    list_display = ['fio', 'objectnlmk', 'email', 'telephone'] 
    search_fields = ('fio','email', 'objectnlmk__objectnlmk')
