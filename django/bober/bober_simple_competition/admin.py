from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from bober_simple_competition.models import *

# Register your models here.
class CompetitionQuestionSetInline(admin.TabularInline):
    model = CompetitionQuestionSet

class CompetitionAdmin(admin.ModelAdmin):
    inlines = [ CompetitionQuestionSetInline ]

class QuestionSetAdmin(admin.ModelAdmin):
    filter_horizontal = ['questions']
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'
    can_delete = False
    filter_horizontal = ['created_codes', 'received_codes', 'used_codes', 'managed_profiles', 'questions', 'question_sets', 'created_question_sets']

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Competitor)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(ResourceCache)
admin.site.register(Resource)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(ShortenedCode)
# admin.site.register(Profile)
