from django.urls import path
from a_home.views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("member-role/<tenant_id>", tenant_member_role, name="member_role"),
]
