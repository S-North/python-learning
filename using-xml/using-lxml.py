from lxml import etree

compendium = etree.parse(r'C:\Users\Stuart\Documents\Python\python-learning\using-xml\compendiums\test-monsters.xml')
root = compendium.getroot()
# compendium = ET.parse('compendiums/items.xml')
# print(root.xpath("//monster[starts-with(name, 'Archmage')]"))

print (root[0][0].tag)
for index, elem in zip(range(1, len(compendium.xpath("/compendium/monster/name/text()"))), compendium.xpath("/compendium/monster/name/text()")):
    print (str(index).ljust(4), elem)

monster = root.xpath('//name[. = "Archmage"]/..')[0] # search for a text string then use ../ to get the parent object
print(monster.tag)
print(monster.find('hp').text)
for elem in monster:
    if len(elem.text) > 0:
        print(elem.text)
# [text()="Archmage"]'))
"""
https://mundrisoft.com/tech-bytes/write-xpath-using-text-and-text-functions-in-selenium/
/       represents a separator (folder/depth)
//      represents any number of separators
.       current item
..      parent item
@       contents of named attribute
text()  contents of text area
[]      conditional e.g. [@attr =]

Methods
.tag    get name of element
.text   get contents of element
.
"""
print("\n\nGet the name of actions")
actions = monster.xpath('action')
# print(actions)
print(actions[0][0].text)
print(monster.xpath('name/text()'))
print(monster.xpath('action/name/text()'))
print(monster.xpath('trait/name/text()'))
# for action in actions:
#     print(action.xpath('name/text()'))
