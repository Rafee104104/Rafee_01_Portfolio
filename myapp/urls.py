from django.urls import path
from .views import *
urlpatterns = [
    path('',registration,name='registration'),
    path('signin/',signin,name='signin'),
    path('user_logout/',user_logout,name='user_logout'),
    path('homepage/',homepage,name='homepage'),
    path('addProfile/',addProfile,name='addProfile'),
    path('editProfile/<int:id>',editProfile,name='editProfile'),
    path('deleteProfile/<int:id>',deleteProfile,name='deleteProfile'),
    path('addEducation/',addEducation,name='addEducation'),
    path('editEducation/<int:id>',editEducation,name='editEducation'),
    path('deleteEducation/<int:id>',deleteEducation,name='deleteEducation'),
    path('addExperience/',addExperience,name='addExperience'),
    path('editExperience/<int:id>',editExperience,name='editExperience'),
    path('deleteExperience/<int:id>',deleteExperience,name='deleteExperience'),
    path('addProject/',addProject,name='addProject'),
    path('editProject/<int:id>',editProject,name='editProject'),
    path('deleteProject/<int:id>',deleteProject,name='deleteProject'),
    path('addSkill/',addSkill,name='addSkill'),
    path('editSkill/<int:id>',editSkill,name='editSkill'),
    path('deleteSkill/<int:id>',deleteSkill,name='deleteSkill'),
    path('contact/',contact,name='contact')
]