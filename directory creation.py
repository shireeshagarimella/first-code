import os
import datetime
import random
import string
print("slno".ljust(10, " "), "file name".ljust(40, " "), "created at".ljust(40, " "), "directory".ljust(60, " "))
for n in range(10):
    now = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    p = "C:\\Users\\VAMSI\\Desktop\\newdir\\" + now + ".txt"
    new_dir = "C:\\Users\\VAMSI\\Desktop\\newdir"
    num_chars = 104857600
    fn = open(p, 'w+')
    while os.path.getsize(p) < num_chars:
        str_ran = ''.join(random.choices(string.ascii_letters + string.digits, k=512))
        fn.write(str_ran)
        os.path.getsize(p)
    print(str(n).ljust(10, " "), now.ljust(40, " "), new_dir.ljust(40, " "), p.ljust(60, " "))
