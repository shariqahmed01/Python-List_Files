import os, csv

f=open("/home/user/.../names.csv",'r+')
w=csv.writer(f)
for path, dirs, files in os.walk("/home/user/.../TargetFolder/"):
    for filename in files:
        w.writerow([filename])