import os
filedir = "/home/nathanlee/Workspace/EAStory/templates/"
filelist = os.listdir(filedir)
for file in filelist:
    print(file)

    userchoice = input('Do you want to edit this file? ')
    if userchoice == '':
        filename = file[:-5]

        htmlfile = open(filedir + file, 'w')

        formattedtitle = input('Title: ')

        formattedparagraph = ''''''
        while True:
            paragraph = input('Paragraph: ')
            if paragraph == '':
                break
            paragraph = '<h5>' + paragraph + '</h5>\n'
            formattedparagraph = formattedparagraph + paragraph + '\n'

        formattedbuttonlist = ''''''

        while True:
            button = input('Button Name: ')
            buttonurl = input('Button URL: ')
            if button == '':
                break
            formattedbutton = '<a href=\"{{% url \'{}\' %}}\" class=\"btn btn-primary\">{}</a>\n'.format(buttonurl, button)
            print(formattedbutton)
            formattedbuttonlist = formattedbuttonlist + formattedbutton
        print(formattedtitle, formattedparagraph, formattedbuttonlist)
        htmltemplate = '''
{{% extends 'index.html' %}}

{{% block content %}}
    {}
    {}
    {}
{{% endblock content %}}
        '''.format(formattedtitle, formattedparagraph, formattedbuttonlist)
        print(htmlfile)
        print(htmltemplate)
        userinput = input("Continue? ")
        if userinput == 'yes':
            htmlfile.write(htmltemplate)
            htmlfile.close()
        else:
            break
    else:
        continue
