from django.urls import path
from . import views

urlpatterns = [
    path('presenttagstory', views.presenttagstory, name='presenttagstory'),


    path('', views.background, name='background'),


    path('returntocrimescene', views.returntocrimescene, name='returntocrimescene'),


    path('techtechiesshop', views.techtechiesshop, name='techtechiesshop'),


    path('interviewsuspects', views.interviewsuspects, name='interviewsuspects'),


    path('continueinvestigating', views.continueinvestigating, name='continueinvestigating'),


    path('leave', views.leave, name='leave'),


    path('crimesceneinvestigation', views.crimesceneinvestigation, name='crimesceneinvestigation'),


    path('bloodonchopsaw', views.bloodonchopsaw, name='bloodonchopsaw'),


    path('eabathroom', views.eabathroom, name='eabathroom'),


    path('securityfootage', views.securityfootage, name='securityfootage'),


    path('testtheredliquid', views.testtheredliquid, name='testtheredliquid'),


    path('thetags', views.thetags, name='thetags'),


    path('handwriting', views.handwriting, name='handwriting'),


    path('investigateot', views.investigateot, name='investigateot'),


    path('otbasement', views.otbasement, name='otbasement'),


    path('chopsawfingerprints', views.chopsawfingerprints, name='chopsawfingerprints'),


    path('contentsoftheboxes', views.contentsoftheboxes, name='contentsoftheboxes'),


    path('fingerprintsonpackages', views.fingerprintsonpackages, name='fingerprintsonpackages'),


    path('voiceprintanalysis', views.voiceprintanalysis, name='voiceprintanalysis'),


    path('convictform', views.convictionform, name='convictform'),


    path('dnaevidence', views.dnaevidence, name='dnaevidence'),

]
