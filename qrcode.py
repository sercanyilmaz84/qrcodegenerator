import pyqrcode 
import png 
from pyqrcode import QRCode
import optparse


def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-u", "--url", dest="website_url", help= "Enter a url")
    options = parse_object.parse_args()[0]
    if not options.website_url:
        print("-u, you must enter an url")
    return options
 
site_info = user_input()
url = site_info.website_url

def createqr(url):
	site = pyqrcode.create(url)
	#site.svg("myqr.svg", scale = 8)
	site.png('createdqr.png', scale = 6)

user_input()
createqr(url)