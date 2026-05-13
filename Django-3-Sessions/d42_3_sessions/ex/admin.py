from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyCustomUser, ModelTip

admin.site.register(MyCustomUser, UserAdmin)



class ModelTipAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'date', 'display_upvotes_count', 'display_downvotes_count')
    filter_horizontal = ('upvotes', 'downvotes')
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None:
            return obj.author == request.user
        return super().has_delete_permission(request, obj)
    
    def display_upvotes_count(self, obj):
        
        return obj.upvotes.count()
    display_upvotes_count.short_description = "Total Upvotes"
    
    def display_downvotes_count(self, obj):
        return obj.downvotes.count()
    display_downvotes_count.short_description = "Total Downvotes"
    
    def has_change_permission(self, request, obj=None):
        
        if request.user.is_superuser:
            return True

        if obj is not None:
            return obj.author == request.user
        return super().has_change_permission(request, obj)


admin.site.register(ModelTip, ModelTipAdmin)

# Register your models here.
# tips_controle
# tiptip@1