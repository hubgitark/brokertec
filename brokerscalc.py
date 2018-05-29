print("我爱北京天安门")
import re

rawtxt = open("tradata.txt")
tradata = dict()

#load data into trade database
i = 0
for line in rawtxt:
    tradata[str(i)] = line.split()
    i = i+1 
linecount = i    
print(linecount)

#calculate total brokerage fee and amount
i = 0
sumfee = 0
sumamt = 0
for i in range(linecount):
    curline = tradata[str(i)]
    curamt = 0
    #clean data e.g. '1000w'
    if curline[5].endswith('w'): 
        actline = list(curline[5])
        actline.remove('w')
        curamt = float(''.join(actline))
    elif curline[5].endswith('万'): 
        actline = list(curline[5])
        actline.remove('万')
        curamt = float(''.join(actline))
    else: 
        try: curamt = float(curline[5])
        except: print(curamt)
    sumamt = sumamt + curamt
    
    #e.g. 203d
    if curline[0].endswith('d'): 
        #clean data
        actline = list(curline[0])
        actline.remove('d')
        curterm = int(''.join(actline))
        if curterm <= 30: sumfee = sumfee + curamt*0.00001
        if curterm > 30: sumfee = sumfee + curamt*0.00003    
    #e.g. 4y
    if curline[0].endswith('y'): 
        #clean data
        actline = list(curline[0])
        actline.remove('y')
        #if actline[-3] == '+': 
            #curterm = float(''.join(re.findall('[0-9]+?',''.join(actline))))/100
        #elif actline[-4] == "+":
            #curterm = float(''.join(re.findall('[0-9]+?',''.join(actline))))/100
        if actline[-3] == '+' or actline[-4] == "+":
            curterm = float(''.join(actline[0]+actline[1]+actline[2]))+float(actline[-2])
        else:
            curterm = float(''.join(actline))
        if curterm <= 5: sumfee = sumfee + curamt*0.00005
        if curterm > 5: sumfee = sumfee + curamt*0.0001
        
print("Total Commission(unit:万):",sumfee)
print("Total Amount:(unit:亿)",sumamt/10000)