import random
ls = ['corgi', 'labrador', 'poodle', 'jack russel']
out=random.choices(ls,weights=[10,1,1,0],k=5)
print(out)
