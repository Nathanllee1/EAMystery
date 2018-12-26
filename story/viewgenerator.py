import os
filelist = os.listdir("/home/nathanlee/Workspace/EAStory/templates/")

viewfile = ''''''

for file in filelist:
    title = file[:-5]
    returnfunction = '''
    def %s(request):
        return render(request, '%s')
    ''' % (title, file)
    print(returnfunction)

for file in filelist:
    title = file[:-5]

    returnurl = '''
    path('%s', views.%s, name='%s'),
    ''' % (title, title, title)
    print(returnurl)

for file in filelist:
    openedfile = open('/home/nathanlee/Workspace/EAStory/templates/' + file, 'w')
    openedfile.write(
    '''
{% extends 'index.html' %}

{% block content %}
    <a href='' class='btn btn-primary'></a>
{% endblock content %}
    '''
    )
    openedfile.close()
