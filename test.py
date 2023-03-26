import shutil, os
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')
shutil.copy('C:\\eggs.txt', 'C:\\delicious\\eggs2.txt')