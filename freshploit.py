#!/usr/bin/python
import httplib
import urlparse
import sys
import datetime
from BeautifulSoup import BeautifulSoup as soup
"""
Freshploit 
by k3170makan

Freshploit fetches the latest vulnerability reports for you from (inj3ct0r) 1337day.com 
and prints them neatly on your terminal screen

Twitter:k3170makan
Web:k3170makan.blogspot.com
"""
class freshploits:
	def __init__(self):
		return
	"""Return the parsed links neatly printed
	date -- the date in yyyy-mm-dd format
	"""
	def getSploitsForDate(self,date):
		BASE_URL="http://1337day.com/webapps"
		parse=urlparse.urlparse(BASE_URL)
		h = httplib.HTTP(parse.netloc)
		h.putrequest('GET',"/date/"+date)
		h.putheader('Host',parse.netloc)
		h.putheader('Accept','text/html')
		h.putheader('Connection','keep-alive')
		h.endheaders()
		try:
			response=h.getreply()
		except:
			return "Problem getting reply, could be your internet set up"
		html=h.getfile().read()
		#uncomment the following if you are having problems getting the page
		#in later versions i will use the info for error reporting
		#for i in response: 
		#	sys.stderr.write(str(i)+'\n')
		#print "data length :",len(html)
		return self.getLinks(html)
	def getLinks(self,page): #in later versions i plan to make a more comprehensive interpretation of the page ;)
		exploit_table = soup(page).findAll("tr")
		for exploit in exploit_table:
			ex=exploit.contents[1]
			ex=soup(str(ex))
			anchor=str(ex.a)
			if anchor != 'None':
				descr = anchor[anchor.index('>')+1:-4]
				link = anchor.split(" ")[1].replace("href=",'').replace("\"",'')
				sys.stderr.write("[%s]%shttp://www.1337day.com%s\n" % (descr,' '*(90-(len(descr)+len(link))),link))
if __name__ == "__main__":
	print ".::Freshploit::."
	date = datetime.datetime.now().strftime("%Y-%m-%d")
	print "Getting vulnerability reports on ",date
	print '-'*120
	fs = freshploits()
	fs.getSploitsForDate(date)
	print '-'*120
