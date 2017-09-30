from django.contrib import admin
from .models import Summary, Experience, School, Skill, Certification

# Register your models here.

admin.site.register(Summary)
admin.site.register(Experience)
admin.site.register(School)
admin.site.register(Skill)
admin.site.register(Certification)
