import os
filedir = "/home/nathanlee/Workspace/EAStory/templates/"
filelist = os.listdir(filedir)
for file in filelist:
    print(file)

    userchoice = input('Do you want to edit this file? ')
    if userchoice == '':
        filename = file[:-5]

        htmlfile = open(file, 'w')

        formattedtitle = '<h1>' + filename + '</h1>'

        formattedparagraph = ''''''
        while True:
            paragraph = input('Paragraph: ')
            if paragraph == '':
                break
            paragraph = '<h5>' + paragraph + '</h5>'
            formattedparagraph = formattedparagraph + paragraph + '\n'

        formattedbuttonlist = ''''''

        while True:
            button = input('Button Name: ')
            buttonurl = button.replace(" ", "").lower()
            if button or buttonurl == '':
                break
            formattedbutton = '<a href=\"{% url \'%s\' %}\" class=\"btn btn-primary\">%s</a>' % (buttonurl, button)
            print(formattedbutton)
            formattedbuttonlist = formattedbuttonlist + formattedbutton

        htmltemplate = '''
{% extends 'index.html' %}

{% block content %}
    %s
    %s
    %s
{% endblock content %}

        ''' % (str(formattedtitle), str(formattedparagraph), str(formattedbuttonlist))

        print(htmltemplate)
        userinput = input("Continue? ")
        if userinput == 'yes':
            htmlfile.write(htmltemplate)
        else:
            break
    else:
        continue


