# from https://stackabuse.com/reading-and-writing-xml-files-in-python/
import xml.etree.ElementTree as ET
tree = ET.parse('compendiums/items.xml')
root = tree.getroot()

# one specific item attribute
print('Item #2 attribute:')
print("print(root[0][1].attrib)")
print(root[0][1].attrib) # returns the attribute as a dictionary
print(root[0][1].attrib['name']) # so we can get the value like this

# all item attributes
print('\nAll attributes:')
print("""
for elem in root:
    for subelem in elem:
        print(subelem.attrib)
""")
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

# one specific item's data
print('\nItem #2 data:')
print("print(root[0][1].text)")
print(root[0][1].text)

# all items data
print('\nAll item data:')
print("""
for elem in root:
    for subelem in elem:
        print(subelem.text)
""")
for elem in root:
    for subelem in elem:
        print(subelem.text)

# finding stuff
print("\nfinding stuff")
for elem in root:
    print(elem.find('item').get('name'))

## with the monster data
## .....................
print("\n"*2 + "."*70)
compendium = ET.parse('compendiums/test-monsters.xml')
root = compendium.getroot()

print(f"Print the value of the 'version' attribute on the root element: {root.attrib['version']}")
print(f"Print the value of the 'version' attribute on the first child: {root[0].attrib['version']}")
print(f"Print the text of the first child pf the first child: {root[0][0].text}")

print("\nfinding stuff")
for elem in root:
    print(elem.find('name').text)

print("\nFinding actions")
monster = root[0]
for elem in monster.findall('action'):
    print(elem.tag)
    print(elem.find('name').text)
    print(elem.find('text').text)
    print(elem.find('attack').text)

# Time to do some deeper reading https://docs.python.org/3/library/xml.etree.elementtree.html

print(monster.tag)
for child in monster:
    print(child.tag)

# for elem in monster.findall(".='Blue Mage'"):
#     print(elem.text)
# tried using the xpath for elementtree which documentation says is supported but it throws an error. Might look at lxml
# was trying to select an element based on its text content e.g. <monster><name>Blue Mage</name></monster> then get its parent. i.e. find a moster by its name.
