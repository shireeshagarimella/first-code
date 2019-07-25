import os
import shutil
import logging

logging.basicConfig(filename='duplicates', level=logging.INFO)


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        print(s)
        d = os.path.join(dst, item)
        print(d)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
            logging.info("{} copying source file".format(s))
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy(s, d)
                logging.info("{} copying to destination".format(d))


copytree("C:\\Users\\VAMSI\\Desktop\\newdir", "C:\\Users\\VAMSI\\Desktop\\copied")