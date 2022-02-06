from django.contrib import admin
from .models import Project, About, Experience
from django.contrib.auth.models import Group
from django.contrib.auth.models import User



# Register your models here.
class MyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.register(Project)
admin.site.register(About, MyAdmin)
admin.site.register(Experience)

