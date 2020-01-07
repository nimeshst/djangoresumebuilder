from django.urls import path
from .views import home
from .views import UserDetails
from .views import experience
from .views import education
from .views import extracurricular
from .views import skills
from .views import project
# django project might have multiple of apps so 
# in order to differtiate between them and tell
# django which url and view to encounter we need to set our
# application namespace

app_name = 'resumebuilder'

urlpatterns = [
	path('', home, name='home'),
	path('UserDetails/',UserDetails, name='UserDetails'),
	path('Experience/', experience, name = 'experience'),
	path('Education/' ,education, name = 'education'),
	path('skills/', skills, name = 'skills'),
	path('extracurricular/', extracurricular, name = 'extracurricular'),
	path('project/', project, name = 'project'),
]