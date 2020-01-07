from .models import UserDetails
from .models import Experience
from .models import Education
from .models import Projects
from .models import Languages
from .models import Hobbies
from .models import Skills
from django.forms import ModelForm


class UserDetailForm(ModelForm):
	class Meta:
		model = UserDetails
		exclude = ['user']


class ExperienceForm(ModelForm):
	class Meta:
		model = Experience
		exclude = ['user']


class EducationForm(ModelForm):
	class Meta:
		model = Education
		exclude = ['user']


class ProjectForm(ModelForm):
	class Meta:
		model = Projects
		exclude = ['user']


class HobbiesForm(ModelForm):
	class Meta:
		model = Hobbies
		exclude = ['user']


class LanguagesForm(ModelForm):
	class Meta:
		model = Languages
		exclude=['user']


class SkillsForm(ModelForm):
	class Meta:
		model = Skills
		exclude = ['user']