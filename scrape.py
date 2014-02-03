import urllib2
import re
from mechanize import Browser

ROMAN_NUMERAL_REGEX = re.compile(r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$');

def getShakespeareSonnets():
	remote = "http://www.gutenberg.org/cache/epub/1041/pg1041.txt";
	titlestr = "by William Shakespeare"
	endstr = "End of The Project Gutenberg Etext of Shakespeare's Sonnets"
	
	# get remote file
	u = urllib2.urlopen(remote);
	localCopy = u.read();
	u.close();
	
	pos = localCopy.rfind(titlestr)+len(titlestr)
	endpos = localCopy.rfind(endstr)
	# remove whitespace and keep only the interesting text
	localCopy = [ s.lstrip().rstrip() for s in localCopy[pos:endpos].split('\r\n') if len(s)>0 ];
	
	# find indices of roman numerals
	sonnet_starts = []
	k = 0;
	for line in localCopy:
		if re.match(ROMAN_NUMERAL_REGEX,line):
			sonnet_starts.append(k)
		k += 1
	
	print localCopy
	print sonnet_starts

def main():
	getShakespeareSonnets()
	
if __name__ == "__main__":
	ret = main()
	if (ret is None):
		print "OK"
	else:
		print "Script didn't execute properly"