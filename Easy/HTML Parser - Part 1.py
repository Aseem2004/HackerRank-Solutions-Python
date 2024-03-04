from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print("Start :", tag)
        if attrs:
            for i in attrs:
                print('-> '+' > '.join(list(map(str,i))))

    def handle_endtag(self,tag):
        print("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for i in attrs:
                print('-> '+' > '.join(list(map(str,i))))

parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())