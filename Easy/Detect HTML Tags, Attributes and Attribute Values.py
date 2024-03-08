from html.parser import HTMLParser

def printattrs(tag,attrs):
    print(tag)
    [print(f'-> {attr} > {val}') for (attr, val) in attrs]

class MyHTMLParser(HTMLParser):
        
    def handle_starttag(self,tag,attrs):
        printattrs(tag,attrs)
    
    def handle_startendtag(self,tag,attrs):
        printattrs(tag,attrs)
        
x=MyHTMLParser()
x.feed("".join([input() for i in range(int(input()))]))