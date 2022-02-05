bob = {'name' : 'bob smith', 'age' : 40, 'pay': 30000, 'job': 'dev'}
sue = {'name' : 'sue jones', 'age' : 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name' : 'tom', 'age' : 50, 'pay': 0, 'job': None}

# baza dannix
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])

dbfilename = 'people-file'
ENDDB = ' enddb. '
ENDREC = ' endrec. '
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
    "сохраняет базу данных в файл"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()
def loadDbase(dbfilename=dbfilename):
    "восстанавливает данные, рекноструируя базу данных"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from initdata import db
    storeDbase(db)










































