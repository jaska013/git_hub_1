bob = ['bob smith', 42, 30000, 'software']
sue = ['sue jones', 45, 40000, 'hardware']
print(bob[0], sue[2])
print(bob[0].split()[-1])
sue[2] *= 1.25


people = [bob, sue]
for person in people:
    print(person)


print(people[1][0])

for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20


for person in people: print(person[2])


pays = [person[2] for person in people]
print(pays)

# gdeto oshibka bor
# pays = map((lamba x: x[2]), people)
# print(list(pays))

print(sum(person[2] for person in people))

people.append(['tom', 50, 0, 'none'])
print(len(people))
print(people[-1][0])


name, age, pay = range(3)
bob = ['bob smith', 42, 10000]
print(bob[name])
print(pay, bob[pay])

bob = [['name', 'bob smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'sue jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
for person in people:
    print(person[0][1], person[2][1])

print([person[0][1] for person in people])


for person in people:
    print(person[0][1].split()[-1])
    person[2][1] *= 1.10

for person in people: print(person[2])



for person in people:
    for (name,value) in person:
        if name == 'name': print(value)



def field(record,label):
    for(fname,fvalue) in record:
        if fname == label:
            return fvalue
print(field(bob,'name'))
print(field(sue,'pay'))


for rec in people:
    print(field(rec,'age'))



bob = {'name': 'bob smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'sue jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
print(bob['name'],sue['pay'])

print(bob['name'].split()[-1])
sue['pay'] *= 1.10
print(sue['pay'])


sue = {}
sue['name']='sue jones'
sue['age']=45
sue['pay']=40000
sue['job']='hdw'
print(sue)


# names = ['name', 'age', 'pay', 'job']
# value = ['sue jones', 42, 40000, 'hdw']
# print(list(zip(name,values)))

bob = {'name': 'bob smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'sue jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

people = [bob,sue]
for person in people:
    print(person['name'], person['pay'], sep=', ')

for person in people:
    if person['name'] == 'sue jones':
        print(person['pay'])

names = [person['name'] for person in people]
print(names)

print(list(map((lambda x: x['name']), people)))

print(sum(person['pay'] for person in people))


print([rec['name'] for rec in people if rec['age'] >= 45])

print([(rec['age'] **2 if rec['age'] >=45 else rec['age']) for rec in people])

G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G.__next__())


for person in people:
    print(person['name'].split()[-1])
    person['pay'] *= 1.10

for person in people: print(person['pay'])

bob2 = { 'name' : {'first': 'bob', 'last': 'smith'},
         'age': 42,
         'job': ['software', 'writing'],
         'pay': (40000,50000)}


for job in bob2['job']: print(job)
print(bob2['job'][-1])

bob2['job'].append('janitor')
print(bob2)

bob = dict(name ='bob smith', age = 42, pay = 30000, job = 'dev')
sue = dict(name ='sue jones', age = 45, pay = 40000, job = 'hdw')
print(bob)

db = {}
db['bob'] = bob
db['sue'] = sue
print(db)
print(db['bob']['name'])
print(db['sue']['pay'])
db['sue']['pay'] = 50000
print(db['sue']['pay'])


import pprint
pprint.pprint(db)

for key in db:
    print(key, '=>', db[key]['name'])




































































