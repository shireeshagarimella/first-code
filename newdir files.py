import os
import datetime
import random
import string
import logging
logging.basicConfig(filename='logging_files', level=logging.INFO)
y = {}
q = input("directory for the files is:")
x = len([name for name in os.listdir(q) if os.path.isfile(os.path.join(q, name))])
new_dir = os.path.getsize(q)

for i in os.listdir(q):
    path = os.path.join(q, i)
    new_dir += os.path.getsize(path)

if new_dir >= 314572800:
    filesToRemove = [os.path.join(q, f) for f in os.listdir(q)]
    for f in filesToRemove:
        os.remove(f)
        logging.info("%s file deleted", f)

for n in range(10):
    now = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    p = q + "\\" + now + ".txt"
    fn = open(p, 'w+')
    while os.path.getsize(p) < 10485760:
        str_ran = ''.join(random.choices(string.ascii_letters + string.digits, k=512))
        fn.write(str_ran)
        os.path.getsize(p)
    y[now] = p

print("sl no".ljust(10, " "), "file name".ljust(40, " "), "created at".ljust(60, " "), "directory".ljust(60, " "))

c = 1
for a in y:
    print(str(x + c).ljust(10, " "), a.ljust(40, " "), q.ljust(60, " "), y[a].ljust(60, " "))
    logging.info("%s file created", y[a])
    c = c + 1
