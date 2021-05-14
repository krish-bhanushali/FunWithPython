#pip install -r requirements.txt
import pyttsx3
import PyPDF2

#add pdf files in the project directory

book=open('pdf-test.pdf', 'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
#print(pages)
speaker=pyttsx3.init()
page=pdfreader.getPage(0)
text=page.extractText()
print('saying')
speaker.say(text)
speaker.runAndWait()
