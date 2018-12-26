from django.shortcuts import render

# Create your views here.


def presenttagstory(request):
        return render(request, 'presenttagstory.html')


def background(request):
    return render(request, 'background.html')


def returntocrimescene(request):
    return render(request, 'returntocrimescene.html')


def techtechiesshop(request):
    return render(request, 'techtechiesshop.html')


def interviewsuspects(request):
    return render(request, 'interviewsuspects.html')


def index(request):
    return render(request, 'index.html')


def continueinvestigating(request):
    return render(request, 'continueinvestigating.html')


def leave(request):
    return render(request, 'leave.html')


def crimesceneinvestigation(request):
    return render(request, 'crimesceneinvestigation.html')


def bloodonchopsaw(request):
    return render(request, 'bloodonchopsaw.html')


def eabathroom(request):
    return render(request, 'eabathroom.html')


def securityfootage(request):
    return render(request, 'securityfootage.html')


def testtheredliquid(request):
    return render(request, 'testtheredliquid.html')


def thetags(request):
    return render(request, 'thetags.html')


def handwriting(request):
    return render(request, 'handwriting.html')


def investigateot(request):
    return render(request, 'investigateot.html')


def otbasement(request):
    return render(request, 'otbasement.html')


def chopsawfingerprints(request):
    return render(request, 'chopsawfingerprints.html')


def contentsoftheboxes(request):
    return render(request, 'contentsoftheboxes.html')


def fingerprintsonpackages(request):
    return render(request, 'fingerprintsonpackages.html')


def voiceprintanalysis(request):
    return render(request, 'voiceprintanalysis.html')


def convictionform(request):
    return render(request, 'convictionform.html')


def dnaevidence(request):
    return render(request, 'dnaevidence.html')
