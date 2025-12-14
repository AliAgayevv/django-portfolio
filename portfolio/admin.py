from django.contrib import admin


from django.contrib import admin
from .models import TechStack, SocialMedia, Project, ContactMessage, AboutMe

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'years_experience', 'location']
    
    def has_add_permission(self, request):
        # Yalnız 1 AboutMe obyekti olmalıdır
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency']
    list_editable = ['proficiency']
    search_fields = ['name']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url']
    list_filter = ['platform']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'is_featured']
    list_filter = ['is_featured', 'created_date']
    search_fields = ['title', 'short_description']
    list_editable = ['is_featured']
    filter_horizontal = ['technologies']
    date_hierarchy = 'created_date'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):

        return False