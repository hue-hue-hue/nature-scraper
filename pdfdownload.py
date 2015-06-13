import urllib
import os.path

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

def download_file(download_url):
    web_file = urllib.urlopen(download_url)
    return web_file.read() 
'''
#########################################################################################
#								get bio papers											#
#																						#
#########################################################################################
BioDLString = ""
index = 40
while index > 0:
	BioDLString = BioDLString + download_file('http://www.nature.com/search?article_type=research&journal=ncb&order=relevance&q=biology&page='+str(index))
	index = index - 1

print "finding bio article links..."
#find all links to articles
BiolinkList = []
for item in BioDLString.split(" itemprop=url"):
	if "href=http://www.nature.com/ncb/journal/" in item:
		BiolinkList.append(item[ item.find("http://www.nature.com/ncb/journal/"): ])

print "converting bio article links to pdf links..."
#change article link into pdf link
BioPDFList = []
for link in BiolinkList:
	link1 = link.replace('full', 'pdf')
	link2 = link1.replace('html', 'pdf')
	BioPDFList.append(link2)

print "saving pdfs to bioFolder"
#save all pdfs into folder
counter = 0
for pdf in BioPDFList:
	counter = counter + 1
	if os.path.isfile("bioFolder/pdf"+str(counter)+".pdf") == False:
		urllib.urlretrieve(pdf, "bioFolder/pdf"+str(counter)+".pdf")

print "appending pdfs to BioPlainText.txt"
#for each pdf in folder, convert to plain text and save into its own plaintext file
failedIndex = 0
while counter > 0:
	f = open("bioFolder/txt"+str(counter)+".txt", 'w')
	try:
		f.write(convert_pdf_to_txt("bioFolder/pdf"+str(counter)+".pdf"))
		counter = counter - 1
	except e:
		print "the"+str(counter)+"-th paper did not convert"
		failedIndex += 1
		counter = counter - 1
	f.close()
print "a total of"+str(failedIndex)+"papers did not convert"
'''
#########################################################################################
#								get physics papers										#
#																						#
#########################################################################################
PhysicsDLString = ""
index = 40
while index > 0:
	PhysicsDLString = PhysicsDLString + download_file('http://www.nature.com/search?article_type=research&journal=nphys&order=relevance&q=physics&page='+str(index))
	index = index - 1

print "finding physics article links..."
#find all links to articles
PhysicslinkList = []
for item in PhysicsDLString.split(" itemprop=url"):
	if "href=http://www.nature.com/nphys/journal/" in item:
		PhysicslinkList.append(item[ item.find("http://www.nature.com/nphys/journal/"): ])

print "converting physics article links to pdf links..."
#change article link into pdf links
PhysicsPDFList = []
for link in PhysicslinkList:
	link1 = link.replace('full', 'pdf')
	link2 = link1.replace('html', 'pdf')
	PhysicsPDFList.append(link2)

print "saving pdfs to physicsFolder"
#save all pdfs into folder 
counter = 0
for pdf in PhysicsPDFList:
	counter = counter + 1
	if os.path.isfile("physicsFolder/pdf"+str(counter)+".pdf") == False:
		urllib.urlretrieve(pdf, "physicsFolder/pdf"+str(counter)+".pdf")

print "appending pdfs to PhysicsPlainText.txt"
#for each pdf in folder, convert to plain text and save into its own plaintext file
failedIndex = 0
while counter > 0:
	f = open('physicsFolder/txt'+str(counter)+'.txt', 'w')
	try:
		f.write(convert_pdf_to_txt("physicsFolder/pdf"+str(counter)+".pdf"))
		counter = counter - 1
	except:
		print "the"+str(counter)+"-th paper did not convert"
		failedIndex += 1
		counter = counter - 1
	f.close()
print "a total of"+str(failedIndex)+"papers did not convert"


