text = """ANSI                   audiodev               markupbase
AptUrl                 audioop                markupsafe
ArgImagePlugin         avahi                  marshal
BaseHTTPServer         axi                    math
Bastion                base64                 md5
BdfFontFile            bdb                    mhlib
BmpImagePlugin         binascii               mimetools
BufrStubImagePlugin    binhex                 mimetypes
CDDB                   bisect                 mimify
CDROM                  bonobo                 mmap
CGIHTTPServer          brlapi                 mmkeys
Canvas                 bsddb                  modulefinder
CommandNotFound        butterfly              multifile
ConfigParser           bz2                    multiprocessing
ContainerIO            cPickle                musicbrainz2
Cookie                 cProfile               mutagen
Crypto                 cStringIO              mutex
CurImagePlugin         cairo                  mx
DLFCN                  calendar               netrc
DcxImagePlugin         cdrom                  new
Dialog                 cgi                    nis
DiscID                 cgitb                  nntplib
DistUpgrade            checkbox               ntpath"""

text = text.split()
text = ["md5"]
for i in text:
	mod = i
	print mod
	modules = map(__import__, mod)
#	try:
#		modules = map(__import__, i)
#	except:
#		print "ok"