import lxml.etree as et
# import xml.etree.ElementTree as et

root = et.Element("knights")
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_tag = et.SubElement(root, "knight", title=title)
        name_tag = et.SubElement(knight_tag, "name")
        name_tag.text = name
        et.SubElement(knight_tag, "color").text = color
        et.SubElement(knight_tag, "quest").text = quest
        et.SubElement(knight_tag, "comment").text = comment

bdoc = et.tostring(root, pretty_print=True)
xml_doc = bdoc.decode()
print(xml_doc)

tree = et.ElementTree(root)
tree.write("knights.xml", pretty_print=True, xml_declaration=True)