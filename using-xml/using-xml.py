from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("compendiums/movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

movies = collection.getElementsByTagName("movie")

for movie in movies:
   print ("*****Movie*****")
   if movie.hasAttribute("title"):
      print ("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)

print("\n"*3)

DOMTree = xml.dom.minidom.parse("compendiums/Archmage")
collection = DOMTree.documentElement
if collection.hasAttribute("version"):
   print ("Version is : %s" % collection.getAttribute("version"))

monsters = collection.getElementsByTagName("monster")
# actions = monsters.getElementsByTagName("action")

for monster in monsters:
   print ("*****Monster*****")
   if monster.hasAttribute("name"):
      print ("Name: %s" % monster.getAttribute("name"))

   type = monster.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   hp = monster.getElementsByTagName('hp')[0]
   print ("HP: %s" % hp.childNodes[0].data)
   ac = monster.getElementsByTagName('ac')[0]
   print ("AC: %s" % ac.childNodes[0].data)
   alignment = monster.getElementsByTagName('alignment')[0]
   print ("Alignment: %s" % alignment.childNodes[0].data)

   action = monster.getElementsByTagName('action')[0]
   print ("Action: %s" % action.childNodes[0].data)

# parse an xml file by name
mydoc = xml.dom.minidom.parse('compendiums/items.xml')

items = mydoc.getElementsByTagName('item')

# one specific item attribute
print('Item #2 attribute:')
print(items[1].attributes['name'].value)

# all item attributes
print('\nAll attributes:')
for elem in items:
    print(elem.attributes['name'].value)

# one specific item's data
print('\nItem #2 data:')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

# all items data
print('\nAll item data:')
for elem in items:
    print(elem.firstChild.data)

print("\n"*2)
# try this out on the archmage xml
compendium = xml.dom.minidom.parse("compendiums/Archmage")
monsters = compendium.getElementsByTagName('monster')
# one specific item attribute
print(f"Monster 1 version: {monsters[0].attributes['version'].value}")

# all item attributes
print("All version attributes")
for elem in monsters:
    print(elem.attributes['version'].value)

# one specific item's data
print(monsters[0].firstChild.data)
print(monsters[0].childNodes[0].data)
print(monsters[0].childNodes[1].data)
print(monsters[0].childNodes[2].data)
print(monsters[0].childNodes[3].data)
print(monsters[0].childNodes[4].data)
print(monsters[0].childNodes[5].data)
