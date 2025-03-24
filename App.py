from docx.api import Document
from docx.shared import Pt

def listFormat(para):
    para=para.replace("*","")
    return para

def appRun():
    markdown_content=""
    doc=Document('demo.docx')
    heading_flag=False
    mainhead_flag=False
    for para in doc.paragraphs:
        for run in para.runs:
            if (run.font.size == Pt(14)):
                heading_flag = True
                # print("changing flag" , heading_flag)
                break
            else:
                heading_flag=False
            break


        if heading_flag:
            if mainhead_flag:
                markdown_content+="## "+para.text+"\n"
            else:
                markdown_content+="# "+para.text+"\n"
                mainhead_flag=True

        if heading_flag!=True and not para.text.strip().startswith('*'):
            markdown_content+=para.text+"\n\n"

        if heading_flag!=True and para.text.strip().startswith('*') or para.style.name==('List Bullet') or para.text.startswith('•'):
            markdown_content+="* "+listFormat(para.text)+"\n\n"
    print(markdown_content)
    try:
        with open('README.md', 'w') as mdFile:
            mdFile.write(markdown_content)
        print("ReadMe file write success")
    except Exception as e:
        print(e)

appRun()