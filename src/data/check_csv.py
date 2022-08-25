import csv

from operator import truediv
def check_csv(fileloc):
    """
    used to check whether the csv has question ,answer, class in all the rows
    
    Args:
        fileloc (String): Full or Relative path of the csv file to be checked

    Returns:
        Boolean:True or False
        False:returns the line numbers which has errors
    """
    reader = csv.reader(open(fileloc,"r",encoding='utf-8'))
    lineno=[]
    k=0
    for row in reader:
        k=k+1
        if len(row)<3 or len(row)>3:
            lineno.append(k)
        else:
            for i in range(0,3):
                if row[i]=='':
                    lineno.append(k)
    if not lineno :
        return True
    else :
        print(lineno)
        return False
        
print(check_csv("src/data/Progress/UGC_2.csv"))#just for demo