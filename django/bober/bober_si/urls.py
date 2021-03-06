from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from bober_simple_competition.models import *
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # 2. pick competition
    url(r'^competitions/(?P<slug>[\w\-_]+)/overview$', 
        views.TeacherOverview.as_view(), name="teacher_overview"),
    url(r'^competitions/(?P<slug>[\w\-_]+)/school_codes_create$', 
        views.SchoolCodesCreate.as_view(), name="school_codes_create"),
)
