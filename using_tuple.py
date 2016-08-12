#元组和列表十分类似，只不过元组和字符串一样是 不可变的 即你不能修改元组
zoo = ('wolf', 'elephant', 'penguin')
print 'Number of animals in the zoo is', len(zoo)
new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All animals in new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoo is', new_zoo[2][2]