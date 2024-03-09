import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    x=0
    if len(node) == 0:
        return len(node.attrib)
    for i in node:
        x+=get_attr_number(i)
    return x+len(node.attrib)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))