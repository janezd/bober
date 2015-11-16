from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from bober_simple_competition.models import *
from bober_simple_competition.views import CompetitionDetail
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # 2. pick competition
    url(r'^competitions/(?P<slug>[\w\-_]+)/overview$', 
        views.TeacherOverview.as_view(), name="teacher_overview"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/overviewx$', 
        views.TeacherOverview.as_view(template_name='bober_si/teacher_overviewx.html'), name="teacher_overviewx"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/profiles_by_school_category$', 
        views.ProfilesBySchoolCategory.as_view(), name="profiles_by_school_category"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/detail$', 
        CompetitionDetail.as_view(), name="competition_detail"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/school_codes_create$', 
        views.SchoolCodesCreate.as_view(), name="school_codes_create"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/teacher_registration$', 
        views.TeacherCodeRegistrationPasswordReset.as_view(), name="teacher_registration"),
    #url(r'^competitions/(?P<slug>[\w\-_]+)/$', 
    #    views.TeacherOverview.as_view(), name="teacher_overview"),
)
