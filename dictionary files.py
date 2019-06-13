import os
import datetime
import random
import string
import logging

logging.basicConfig(filename='logging_files', level=logging.INFO)
q = input("directory for the files is:")
x = len([name for name in os.listdir(q) if os.path.isfile(os.path.join(q, name))])
new_dir = os.path.getsize(q)

for i in os.listdir(q):
    path = os.path.join(q, i)
    new_dir += os.path.getsize(path)

d = {}
if new_dir >= 314572800:
    filesToRemove = [os.path.join(q, f) for f in os.listdir(q)]
    count = 0
    for f in filesToRemove:
        count = count + 1
        file = 'file_' + str(count)
        t2 = datetime.datetime.now().timestamp()
        c = {'created_at': t2, 'size': os.path.getsize(f), 'final_location': q}
        os.remove(f)
        d[file] = c
        logging.info("%s file deleted", f)

b = {}
print("sl no".ljust(10, " "), "file name".ljust(40, " "), "created at".ljust(60, " "), "directory".ljust(60, " "))
for n in range(10):
    s = []
    now = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    p = q + "\\" + now + ".txt"
    fn = open(p, 'w+')
    t = datetime.datetime.now().timestamp()

    while os.path.getsize(p) < 10485760:
        str_ran = ''.join(random.choices(string.ascii_letters + string.digits, k=512000))
        fn.write(str_ran)
        s.append(os.path.getsize(p))

    file = 'file_' + str(x+n+1)
    a = {'created_at': t, 'size': s, 'final_size': os.path.getsize(p), 'final_location': q}
    b[file] = a

    print(str(x + n+1).ljust(10, " "), now.ljust(40, " "), q.ljust(60, " "), p.ljust(60, " "))
    logging.info("%s file created", p)

dic = {'created': b, 'deleted': d}

import json

print(json.dumps(dic, sort_keys=True, indent=4))
