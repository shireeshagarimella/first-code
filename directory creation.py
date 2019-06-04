import os
import datetime
import random
import string
print("slno".ljust(10, " "), "file name".ljust(40, " "), "created at".ljust(60, " "), "directory".ljust(60, " "))
for n in range(10):
    now = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    q = os.getcwd()
    p = q + "\\" + now + ".txt"
    x = len([name for name in os.listdir(q) if os.path.isfile(os.path.join(q, name))])
    num_chars = 104857600
    fn = open(p, 'w+')
    while os.path.getsize(p) < num_chars:
        str_ran = ''.join(random.choices(string.ascii_letters + string.digits, k=512))
        fn.write(str_ran)
        os.path.getsize(p)
    print(str(x+1).ljust(10, " "), now.ljust(40, " "), q.ljust(60, " "), p.ljust(60, " "))
