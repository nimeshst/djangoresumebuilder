from django.contrib import admin
from .models import User ,UserDetails, Experience, Education, Projects, Hobbies, Languages

# Register your models here.
#admin.site.register(User)
admin.site.register(UserDetails)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Projects)
admin.site.register(Hobbies)
admin.site.register(Languages)