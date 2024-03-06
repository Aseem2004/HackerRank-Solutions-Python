from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
            
    def handle_data(self,data):
        if '\n' not in data:
            print(">>> Data")
            print(data)
            
x=""
for i in range(int(input())):
    x+= input().rstrip()
    x+= '\n'
    
parser = MyHTMLParser()
parser.feed(x)
parser.close()