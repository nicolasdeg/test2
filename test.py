# -*- coding: cp1252 -*-
import csv

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

i=0

file = open(r"C:\Users\Niko\Desktop\rekl\data\starter.json","w") 
entete=[]
nb_line =0 

with open(r"C:\Users\Niko\Desktop\test\RDF_FORET_2.txt", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        nb_line=nb_line+1

print spamreader.line_num
with open(r"C:\Users\Niko\Desktop\test\RDF_FORET_2.txt", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    file.write("[\n")
    for row in spamreader:
        if i==0:
            for r in row:
                entete.append(r)
            print len(entete)
            print entete
        elif i ==nb_line-1:        
            k=0
            pk=i
            file.write("    {\n")
            file.write("        \""+"id"+"\": "+str(pk)+",\n")
            for r in row:
                if k==len(entete)-1:
                    if is_number(r)==True:
                        file.write("        \""+entete[k]+"\": "+r+"\n")
                    else:
                        file.write("        \""+entete[k]+"\": \""+r+"\"\n")
                else:
                    if is_number(r)==True:
                        file.write("        \""+entete[k]+"\": "+r+",\n")
                    else:
                        file.write("        \""+entete[k]+"\": \""+r+"\",\n")
                k=k+1
            file.write("    }\n")
        else:        
            k=0
            pk=i
            file.write("    {\n")
            file.write("        \""+"id"+"\": "+str(pk)+",\n")
            for r in row:
                nb_col =(len(entete))-1
                if k==nb_col:
                    if is_number(r)==True:
                        file.write("        \""+entete[k]+"\": "+r+"\n")
                    else:
                        file.write("        \""+entete[k]+"\": \""+r+"\"\n")
                else:
                    if is_number(r)==True:
                        file.write("        \""+entete[k]+"\": "+r+",\n")
                    else:
                        file.write("        \""+entete[k]+"\": \""+r+"\",\n")
                k=k+1
            file.write("    },\n")
        i=i+1
    file.write("]")

file.close()
