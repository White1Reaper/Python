from django.contrib import admin
from .models import Client, Policy, Claim

# Задание 3. Построить отображение моделей в панели администратора, используя различные списки отображения и фильтры.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'start_date', 'end_date', 'customer')
    list_filter = ('start_date', 'end_date')

class ClaimAdmin(admin.ModelAdmin):
    list_display = ('claim_number', 'date_filed', 'description', 'policy')
    list_filter = ('date_filed',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Claim, ClaimAdmin)
