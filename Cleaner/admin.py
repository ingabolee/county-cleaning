from django.contrib import admin
from .models import Employer,Equipment,PaymentDetails,Location,CountyDetails,MyUser
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm


admin.site.register(Employer)
admin.site.register(Equipment)
admin.site.register(PaymentDetails)
admin.site.register(Location)
admin.site.register(CountyDetails)




class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm

	list_display = ('username','email','is_admin')
	list_filter = ('is_admin',)

	fieldsets = (
			(None, {'fields': ('username','email','password')}),
			('Permissions', {'fields': ('is_admin',)})
		)
	search_fields = ('username','email')
	ordering = ('username','email')

	filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)


admin.site.unregister(Group)
