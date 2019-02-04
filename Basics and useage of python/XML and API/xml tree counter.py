from xml.etree import ElementTree

xml_file=input()
tree=ElementTree.fromstring(xml_file)
coub_dict = {'red': 0, 'green': 0, 'blue': 0}

def rec_func(elem,level=1):
    coub_dict[elem.attrib['color']] += level
    for child in elem.getchildren():
        rec_func(child, level+1)

rec_func(tree)

for i in coub_dict.keys():
    print(coub_dict[i],end=' ')