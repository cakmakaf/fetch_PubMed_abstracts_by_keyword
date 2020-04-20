# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from Bio import Entrez
Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
handle = Entrez.egquery(term="cystic fibrosis")
record = Entrez.read(handle)

#for row in record["eGQueryResult"]:
#    print(row["DbName"], row["Count"])
    
def findyear(dpmsg):
    frst=-1
    last=-1
    for i in range(len(dpmsg)):
        if dpmsg[i]<='9' and dpmsg[i]>='0' and last-frst!=3:
            if frst==-1:
                frst=i            
            last=i
        else:
            if not last-frst==3:
                frst=-1
                last=-1
    return int(dpmsg[frst:last+1])    
    
       
        
        


handle = Entrez.esearch(db="pubmed", term="cystic fibrosis", retmax=20000)
record = Entrez.read(handle)
handle.close()
idlist = record["IdList"]    




from Bio import Medline
handle = Entrez.efetch(db="pubmed", id=idlist[0:10000], rettype="medline",retmode="text")
records = Medline.parse(handle)
records = list(records)

handle1 = Entrez.efetch(db="pubmed", id=idlist[10000:], rettype="medline",retmode="text")
records1 = Medline.parse(handle1)
records1 = list(records1)





for record in records:

    xx=findyear(record.get("DP"))    
    print(xx)
    # f  = open(''.join(record.get("PMID", "?"))+".txt", 'w')
    # f.write("Title: "+ ''.join(record.get("TI", "?")))
    # f.write('\n')
    # f.write("Authors: "+ ''.join(record.get("AU", "?")))
    # f.write('\n')
    # f.write("Journal: "+ ''.join(record.get("TA", "?")))
    # f.write('\n')
    # f.write("Date of Publication "+ ''.join(str(xx)))
    # f.write('\n')
    # f.write("Abstract: "+ ''.join(record.get("AB", "?")))
    # f.write('\n')
    # f.write("Keywords: "+ ''.join(record.get("OT", "?")))
    # f.write('\n')
    # f.write("Mesh Terms: "+ ''.join(record.get("MH", "?")))
    # f.close()

for record in records1:

    xx=findyear(record.get("DP"))    
    print(xx)
    # f  = open(''.join(record.get("PMID", "?"))+".txt", 'w')
    # f.write("Title: "+ ''.join(record.get("TI", "?")))
    # f.write('\n')
    # f.write("Authors: "+ ''.join(record.get("AU", "?")))
    # f.write('\n')
    # f.write("Journal: "+ ''.join(record.get("TA", "?")))
    # f.write('\n')
    # f.write("Date of Publication "+ ''.join(str(xx)))
    # f.write('\n')
    # f.write("Abstract: "+ ''.join(record.get("AB", "?")))
    # f.write('\n')
    # f.write("Keywords: "+ ''.join(record.get("OT", "?")))
    # f.write('\n')
    # f.write("Mesh Terms: "+ ''.join(record.get("MH", "?")))
    # f.close()