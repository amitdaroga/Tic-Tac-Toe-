import pdfkit  
from zipfile import ZipFile
import os
# configuring pdfkit to point to our installation of wkhtmltopdf  

def HTMLTOPDF(my_string,tcnumber):
    config = pdfkit.configuration(wkhtmltopdf = r"D:\amit_project\pdfkit\bin\wkhtmltopdf.exe")
    # storing string to pdf file 
    try:
        pdfname=tcnumber+".pdf"
        pdfkit.from_string(my_string, pdfname, configuration = config)
        #pdfkit.from_file('pyhtml.html', 'output3.pdf', configuration = config)
    except Exception as E:
        print(E)
        return ''
    try:
        zipname=tcnumber+".zip"
        with ZipFile(zipname, 'w') as zipObj2:
            zipObj2.write(pdfname)
            os.remove(pdfname)
        return zipname
    except Exception as E:
        print(E)
        return""

  
  





# # import weasyprint
# # pdf = weasyprint.HTML('http://www.google.com').write_pdf()
# # print(len(pdf))


