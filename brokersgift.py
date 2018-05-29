# HelloWorld
print("我爱北京天安门")
import re

# Read through the whole file and identify each deal
rawtxt = open("成交 2017-12.txt")
modict = dict() #a simple scanner that records every line of the rawtxt


count = 0
for line in rawtxt:
    if not (line.startswith('\n') or line.startswith(' ')):
        words = line.split()
        modict[count] = words
        count = count + 1
        
linecount = count
print(linecount)

txt = open('modict.txt',"w")
count = 0
for count in range(linecount): 
    txtline = ''.join(modict[count])+"\n"
    txt.write(txtline)

# Isolate each deal and load them in one line of list   
tradata = dict() #the complete deal database
details = [0,1,2,3,4,5,6,7,8,9,10] #details for each deal

wrt = open('output.txt',"w")

count = 0
numdl = 0 #number of deals registered
while count <= linecount-2:   
    if len(modict[count]) == 7:
        zeroline = modict[count-1] #optional
        firstline = modict[count]
        secondline = modict[count+1]        
    #type 1 format
    #l0 DONE 七十一
    #l1 14.37y   1180156 11铁道06       aaa 4.50 3000 6/30+1 
    #l2 圆周资产 出给 矩阵人寿 
    #l3 麻烦发 矩阵人寿 七十一
        if len(secondline) == 3 and secondline[1] == "出给":
            thirdline = modict[count+2]
            details[0] = firstline[0] #期限
            details[1] = firstline[1] #券号
            details[2] = firstline[2] #券名
            details[3] = firstline[3] #评级
            details[4] = firstline[4] #收益率
            details[5] = firstline[5] #量
            details[6] = secondline[0] #卖方
            details[7] = secondline[2] #买方
            if not thirdline[0].startswith("-"):
                if not len(thirdline) == 7: 
                    details[8] = thirdline[0] #过桥方
            if len(zeroline) == 2 and zeroline[0] == "DONE":
                details[9] = zeroline[1] #我方交易员
            elif not len(zeroline) == 7 and not len(zeroline[0]) > 5: details[9] = zeroline[0]
            details[10] = firstline[6] #交割日期            
            #write into output.txt
            wrtline = details[0]+"	"+details[1]+"	"+details[2]+"	"+details[3]+"	"+details[4]+"	"+details[5]+"	"+details[6]+"	"+details[7]+"	"+details[8]+"	"+details[9]+"	"+details[10]+"\n"
            wrt.write(wrtline)
            
            #tradata[numdl] = details
            numdl = numdl+1
           
     
    #type 2 format
    #l0 DONE 攒暗器
    #l1 35d      041662036 16重庆轨交CP001 aaa 4.00 1000 6/1+0 
    #l2 卖出：武林资管 2厘 
    #l3 买入：起威基金 
    #l4 请求发紫禁城
        elif secondline[0].startswith("卖出"):
            thirdline = modict[count+2]
            details[0] = firstline[0] #期限
            details[1] = firstline[1] #券号
            details[2] = firstline[2] #券名
            details[3] = firstline[3] #评级
            details[4] = firstline[4] #收益率
            details[5] = firstline[5] #量
            #clean "卖方"
            actsecline = list(secondline[0])
            print(count)
            i = 0
            for i in range(3): del actsecline[0]
            details[6] = ''.join(actsecline) #卖方
            #clean "买方"
            actthiline = list(thirdline[0])
            i = 0
            for i in range(3): del actthiline[0]
            details[7] = ''.join(actthiline) #买方           
            if count+3 < linecount: fourthline = modict[count+3]
            if not fourthline[0].startswith("-"):
                if not len(fourthline) == 7: 
                    details[8] = fourthline[0] #过桥方
            if len(zeroline) == 2 and zeroline[0] == "DONE":
                details[9] = zeroline[1] #我方交易员
            elif not len(zeroline) == 7 and not len(zeroline[0]) > 5: details[9] = zeroline[0]
            details[10] = firstline[6] #交割日期
            #write into output.txt
            wrtline = details[0]+"	"+details[1]+"	"+details[2]+"	"+details[3]+"	"+details[4]+"	"+details[5]+"	"+details[6]+"	"+details[7]+"	"+details[8]+"	"+details[9]+"	"+details[10]+"\n"
            wrt.write(wrtline)
            
            numdl = numdl+1
            
    count = count+1  
            
wrt.close()        

    
#print(tradata[0])
print(numdl)





