import webbrowser as wb

class browserManager(object):
    
    link = 'https://www.google.com'
    
    def getLink(self):
        return self.link
    
    def setLink(self, link):
        if(link != None):
            self.link = link
            return link
        else:
            return "none given"
    
    def openBrowser(self, link):
        if(link == None):
            wb.open_new(self.link)
            return "No Link Provided"
        else:
            wb.open_new(link)
            return "Opening: "+link

YouTube = browserManager()
print("This is the beginning of the program")
print("Deafault Address:" + YouTube.getLink())
newAddr = input("New Address:")
if(not newAddr):
    print("No address given")
else:
    print("Changing address to: " + YouTube.setLink(newAddr))
print("New Address: " + YouTube.getLink())
if(not newAddr):
    print("Opening Without a Link: "+YouTube.openBrowser(None))
else:
    print("Opening Link: " + YouTube.openBrowser(YouTube.getLink()))