# importing required modules
import PyPDF2
from TTS import *
from tkinter import filedialog
# creating a pdf file object
def ebookreader():
    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
    pdfFileObj = open(file, 'rb')
        
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
    # printing number of pages in pdf file
    print(pdfReader.numPages)
    number_of_pages = pdfReader.getNumPages()
    for page_number in range(number_of_pages):   # use xrange in Py2
        page = pdfReader.getPage(page_number)
        page_content = page.extractText()
        # pdfReader.write(page_content)
    
    tts(page_content)
    pdfFileObj.close()
