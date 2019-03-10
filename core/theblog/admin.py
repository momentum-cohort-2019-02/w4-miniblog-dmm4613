from django.contrib import admin
from theblog.models import Blog, Blogger

#admin.site.register(Blog)
#admin.site.register(Blogger)

# Define the admin class
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    

# Register the admin class with the associated model
admin.site.register(Blogger, BloggerAdmin)

#Register teh Admin classes for Blog using the decorator
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'date_of_blog')


