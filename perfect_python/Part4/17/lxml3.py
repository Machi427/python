from lxml import etree

nsmap = {None: "http://www.w3.org/2005/Atom"}
new_elem = etree.Element("feed", nsmap=nsmap)
sub1 = etree.SubElement(new_elem, "title")
sub1.text = "my test feed"
sub2 = etree.Element("link", attrib={"href": "http://gihyo.jp"})
new_elem.append(sub2)

print(etree.tounicode(new_elem, pretty_print=True))

