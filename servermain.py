import iot_download
import readfile
import csv
import os

def add_csv(csv_string):
    with open(r'csvfile.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_string)

def compareTime(new, old):
    #check if Time* is a proper flag
    content_new = open("download/"+new, 'r', encoding='latin-1').read()
    content_old = open("download/"+old, 'r', encoding='latin-1').read()    
    pos_new = content_new.find("Time8")
    pos_old = content_old.find("Time8")  
    i = 0
    while(content_new[pos_new+i] == content_old[pos_old+i]) :
        #check if 30 is a proper flag
        if(i >= 30) :
            return 0
        i+=1;
    return 1

csv_list=[]
#need a initial file with "Time8"
filetxt = open('filename_new.txt', 'r')
newfile = filetxt.readline()[:-1]
oldfile = filetxt.readline()[:-1]
if (compareTime(newfile, oldfile)):  #need to be implement by read the content of the file  
    os.remove("download/"+oldfile)
    csv_list=readfile.read("download/"+newfile)
    filetxt.close()
    #filname from bash script here ^^^^^^^
    print("update success")    
    add_csv(csv_list)
else :
    print("no update")
    os.remove("download/"+oldfile)
filetxt.close()