shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have',len(shoplist),'items to purchase.'

print 'These items are',
for item in shoplist:
	print item,
print '\nI also have to buy rice.'

shoplist.append('rice')
print 'My shopping list is',shoplist

shoplist.sort()
print 'Sorted shopping ilst is ',shoplist

print 'The first item I will buy is ',shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'My shopping list is now',shoplist