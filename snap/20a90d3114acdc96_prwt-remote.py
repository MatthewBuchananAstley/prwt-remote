#!/usr/bin/python3
#
# How do you easily see if a certain time is between the start and stop time of a login session 
# and from which host?
# With this script!
#
# It can also summarize the login session times for each week of the year or for one week. 
# 
#
# On the remote host:
# last -F > 'filename'
#
# filename should have entries like this:
# 'username' pts/0        'hostname' Tue Jan 12 14:05:24 2021 - Tue Jan 12 14:06:43 2021  (00:01)
# 'username' pts/0        'hostname' Tue Jan 12 14:03:06 2021 - Tue Jan 12 14:05:13 2021  (00:02)
# 'username' pts/0        'hostname' Tue Jan 12 13:57:57 2021 - Tue Jan 12 13:58:53 2021  (00:00)
#
# Usage: ./prwt.py "last -F output filename" "year" "username" "weeknumber" or "search timestamp"')
#
# For a summary of the login session time spent on a local linux machine see prwt_local.py
#
# 2021 Matthew Buchanan Astley ( matthewbuchanan@astley.nl ) 

 
import os,sys
import datetime
#import timefuncties
import subprocess


try:
    a = sys.argv[1]
    a1 = open(a, "r")
except IndexError:
    #print('Usage: ./prwt.py "last -F output filename" "year" "weeknumber" "username"')
    #print('Usage: ./prwt.py "last -F output filename" "year" "username" "weeknumber" "search timestamp"')
    print('Usage: ./prwt.py "last -F output filename" "year" "username" "weeknumber" or "search timestamp"')
    sys.exit()

try:
    c3 = sys.argv[2]
except IndexError:
    print('Usage: ./prwt.py "last -F output filename" "year" "username" "weeknumber" or "search timestamp"')
    sys.exit()

try:
    c4 = sys.argv[3]
except IndexError:
    print('Usage: ./prwt.py "last -F output filename" "year" "username" "weeknumber" or "search timestamp"')
    sys.exit()


c = { "1" : [], "2" : [], "3" : [], "4" : [], "5" : [], 
      "6" : [], "7" : [], "8" : [], "9" : [], "10" : [], 
      "11" : [], "12" : [], "13" : [], "14" : [], "15" : [],
      "16" : [], "17" : [], "18" : [], "19" : [], "20" : [],
      "21" : [], "22" : [], "23" : [], "24" : [], "25" : [],
      "26" : [], "27" : [], "28" : [], "29" : [], "30" : [],
      "31" : [], "32" : [], "33" : [], "34" : [], "35" : [],
      "36" : [], "37" : [], "38" : [], "39" : [], "40" : [],
      "41" : [], "42" : [], "43" : [], "44" : [], "45" : [],
      "46" : [], "47" : [], "48" : [], "49" : [], "50" : [],
      "51" : [], "52" : [] }

d = { 'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12 }


def ret_mth(self):

    d = { '1' : 31, '2' : self[1], '3' : 31, '4' : 30, '5' : 31, '6' : 30, '7' : 31, '8' : 31, '9' : 30, '10' : 31, '11' : 30, '12' : 31 }  
    return(d[self[0]])


#def dimth(self):
def dimth(self):
    
    a1 = int(self[0]) / 4
    a1_1 = str(a1).split(".")
    
    a2 = int(self[0]) / 100
    a2_1 = str(a2).split(".")
    
    a3 = int(self[0]) / 400
    a3_1 = str(a3).split(".") 

    #d = { '1' : 31, '2' : feb, '3' : 31, '4' : 30, '5' : 31, '6' : 30, '7' : 31, '8' : 31, '9' : 30, '10' : 31, '11' : 30, '12' : 31 }  

    if a1_1[1] != '0':
        #print('28', a1_1)
        #sys.exit()
        feb = 28
        return(ret_mth([self[1],feb]))

    if a2_1[0] != 0:
        #print('29', a2_1) 
        #sys.exit()
        feb = 29
        return(ret_mth([self[1],feb]))
 
    #return(d[self[1]])

#def print_months(year):
#    months = [ "1","2","3","4","5","6","7","8","9","10","11","12" ] 
#    a =  [] 
#    for month in months:
#        cmd = [ "print-weeks-1.0-finance/usr/bin/prd.pl", year, month ] 
#        output = subprocess.check_output(cmd)
#        t = output.decode()
#        if len(month) == 1:
#            month = str(0) + month 
#        b = year + month + "01" + " " + year + month + t
#        a.append(b)
#    return(a)

def print_months(year):

    months = [ "1","2","3","4","5","6","7","8","9","10","11","12" ] 
    a = []
    for month in months:
        self = [ year, month]
        t = dimth(self) 
        if len(month) == 1:
            month = str(0) + month
        b = str(year) + str(month) + "01" + " " + str(year) + str(month) + str(t)
        a.append(b)

    return(a)  

def weeknumber(year,month,day):
    a = datetime.datetime(int(year),int(month),int(day))
    a1 = a.isocalendar()
    return(a1)

def pmt(year):

    a = print_months(year)
    #print("Ja",a)

    months = { "1": [], "2" : [], "3" : [], "4" : [], "5" : [], "6" : [], "7" : [], "8" : [], "9" : [], "10" : [], "11" : [], "12" : [] }

 
    for j,i in enumerate(a):
        j += 1 
        ii = i.split()
        b = ii[1][6:8]
        b1 = [] 
        for iii in range(1,int(b) + 1):
            b1.append(iii)          
        for d in b1:
            months[str(j)].append(d)

    e1 = weeknumber(int(2020),int(12),int(months["12"][-1]))

    if int(e1[1]) != 52:
        e = e1[1]
    else:
        e = 52

    e2 = []
    d1 = []

    for i in range(0,e):
        e2.insert(i,[])   

    e2.insert(0,[])
    for i in months.keys():
        for ii in months[i]:
            a = weeknumber(year,i,ii)
            a1 = int(a[1]) 
            e2[a1].append([year,i,ii,a[1]]) 
        
    a2 = { "1" : "Jan", "2" : "Feb", "3" : "Mar", "4" : "Apr", "5" : "May", "6" : "Jun",  "7" : "Jul", "8" : "Aug", "9" : "Sep","10" : "Oct", "11" : "Nov", "12" : "Dec" }

    if e == '53':
        e3 = range(1,e + 1)
    else: 
        e3 = range(1,e)

    e5 = {}

    for i in e3:
        if e == 53:
            t = []
            t1 = [] 
            for ii in e2[e - 1]:
                if ii[1] == '1': 
                    t.append(ii)
            for iii in e2[e - 1]:
                if iii not in t:
                    t1.append(iii)
        
            for iiii in t:
                t1.append(iiii)
    
            e2[e - 1] = t1

        e4 = e - 1 
     
        if int(e2[i][0][-1]) == int(e4) and a2[e2[i][-1][1]] == "Jan":
            y = int(e2[i][0][0]) + 1
        else:
            y = e2[i][0][0] 

        d = str(e2[i][0][-1]) + " " +  str(e2[i][0][2]) + " " + str(a2[e2[i][0][1]]) + " " + str(e2[i][0][0])  
        d1 = str(e2[i][-1][2]) + " " + str(a2[e2[i][-1][1]]) + " " + str(y)
        e5[str(e2[i][0][-1])] = [ d, d1 ]

    return(e5)

def p_t(self_1):
    import time
    day = { 'Mon' : 0, 'Tue' : 1, 'Wed' : 2, 'Thu' : 3, 'Fri' : 4, 'Sat' : 5, 'Sun' : 6 }
    a = self_1.split()
    a1 = a[3].split(":")
    tm_year = int(a[4])
    tm_mon = int(d[a[1]])
    #tm_mday = int(day[a[0]]) 
    tm_mday = int(a[2]) 
    tm_hour = int(a1[0])
    tm_min = int(a1[1])
    tm_sec = int(a1[2])
    tm_wday = int(day[a[0]])
    tm_yday = int()
    tm_isdst = int()
    t = (tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst)
    e = time.mktime(t)
    #e = time.asctime(t)
    #return(e)
    return(int(e))


a14 = []

def prdat(self):

    d = []

    c = self[0]
    #print(c)
    year = {} 
    for i in c:
        if len(i) > 0: 
            ii = i[0].split()
            year['y'] = ii[-1] 
    #print(year)         
    #year = '' 
    #year = [] 
    for j,i in enumerate(c):
        c1 = j - 1
        c2 = c[c1][0].split()
        #print(c2)
        #print(c2[-1])
        #year = c2[-1]
        #year["year"] = c2[-1]
        #year.append(c2[-1])
        c3 = i[0].split()
        c4 = i[1].split()
        c4_1 = c4[3].split(":")
        c5 = c[c1][1].split()
        a1 = c2[3].split(":")
        a2 = c3[3].split(":")
        a3 = a1[0] + a1[1] 
        a4 = a2[0] + a2[1]

        a5 = c5[3].split(":")
        a5_1 = ''.join(a5) 
        a6 = ''.join(c4_1) 

        if a3 != a4:  
            a5 = i[2].strip("()")
            a6 = a5.split(":")
            d.append(a6) 
        else:
            if a5_1 < a6:
                d.pop()
                e1 = i[2].strip("()")
                e2 = e1.split(":")
                d.append(e2)
    #print(year)
    #sys.exit()
    #print("Ja",d) 

    a7 = int()
    a8 = int()
    #print("JA",year)   
    #print("JA",year["year"])
    #year = 
    #a7_1 = b5a7.pmt(year["year"])
    for i in d:
        a7 += int(i[0])
        a8 += int(i[1])
    #    print("Ja", a7, a8) 
    if a8 > 60:
        a13_1 = round(a8 / 60,2)
    #else:
    #    a13_1 = a8
        a9 = str(a13_1).split(".") 
        a9_1 = str(0) + "." + str(a9[1])
        a9_2 = float(a9_1) * 60
        a9_3 = str(a9_2).split(".")
        a10 = a7 + int(a9[0])
        a12_1 = a9_3[0]
        a13 = str(a10) + ":" + str(a12_1) 
        a14.append(a13)
        #print(self[2],self[1],a13)
        #print(self[2],a7_1[self[1]],a13)
        return([self[2],self[1],a13]) 
    else:
        a13_1 = a8
        a13 = str(0) + ":" + str(a13_1)
        #print(self[2],self[1],a13)
        #print(self[2],a7_1[self[1]],a13)
        return([self[2],self[1],a13]) 
        

#print("Ja",a1) 
#sys.exit()

for i in a1:
    j = i.split()
    #if len(j) == 15:
    #print("JA", j)
    if len(j) == 15:
        #print("JAA", j)
        year = int(j[7])
        month = int(d[j[4]])
        day = int(j[5])
        c1 = datetime.date(year,month,day) 
        c2 = c1.isocalendar()
        b = j[3] + " " + j[4] + " " + j[5] + " " + j[6] + " " + j[7]
        b1 = j[9] + " " + j[10] + " " + j[11] + " " + j[12] + " " + j[13]
        #print("jAA", b, b1)
        #if j[0] == sys.argv[4] and j[7] == sys.argv[2]:
        #if j[0] == sys.argv[3] and j[7] == sys.argv[2]:
        if j[0] == c4 and j[7] == c3:
            #c[str(c2[1])].append( [ b, b1, j[14] ] ) 
            c[str(c2[1])].append( [ b, b1, j[14], j[2] ] ) 

#print(c)
#sys.exit()
#print("Ja",len(c))
#print(c[c4])
##for j,i in enumerate(c[c4]):
##    print(c[c4][j][2])
##self = [ c[c4], c4, sys.argv[4] ] 
##prdat(self)
##sys.exit()

a1 = c.keys() 
a2 = []

for i in a1:
    #self = [ c[i], c4, sys.argv[4] ]
    #self = [ c[i], i, sys.argv[4] ]
    self = [ c[i], i, sys.argv[3] ]
    ii = prdat(self)
    a2.append(ii)

#print("Ja",a2)

year = c3
a_1 = pmt(year)

#a4 = []

a4_1 = []


for i in a2:
    #print(i[1])
    #print("ja",i[0],a_1[i[1]][0], " - ",a_1[i[1]][1],i[2]) 
    #print(a_1[i[0]]) 
    a_2 = a_1[i[1]][0].split()
    #print(a_2)
    a_3 = a_2[1] + " " + a_2[2] + " " + a_2[3]
    #print('''<tr><td>''' + i[0] + '''</td><td>''' + a_1[i[1]][0][0:2] + '''</td><td>''' + a_1[i[1]][0] + ''' - ''' + a_1[i[1]][1] + '''</td><td>''' + i[2] + '''</td></tr>''')  
    ##print('''<tr><td>''' + i[0] + '''</td><td>''' + a_1[i[1]][0][0:2] + '''</td><td>''' + a_3 + ''' - ''' + a_1[i[1]][1] + '''</td><td>''' + i[2] + '''</td></tr>''')  
    #a4.append([ i[0] , a_1[i[1]][0][0:2], a_3, a_1[i[1]][1], i[2] ] ) 
    #print("Ja",i[0], a_1[i[1]][0][0:2], a_3, a_1[i[1]][1], i[2]) 
    a4_1.append([ i[0] , a_1[i[1]][0][0:2].rstrip(), a_3, a_1[i[1]][1], i[2] ] ) 

#print("Ja", a4_1)
#sys.exit() 

res = '' 

try:
    a5 = sys.argv[4]
    try:
        a6 = sys.argv[5]
    except IndexError:
        a6 = ''
    
    if len(a5) > 2:
        a6 = a5 

    t = p_t(a6)
    #print("JA",a6,t)
    a7 = []
    #a8 = [ a6 ]
    #a8 = []
    for i in c.keys():
        if len(c[i]) > 0: 
            #print("ja",c[i])
            for i in c[i]: 
                #print("Ja",i)
                a8 = []  
                a1 = int(p_t(i[0]))
                a2 = int(p_t(i[1]))
                #print("Ja",a1,a2)
                for j in range(a1,a2):
                    #print("Ja", j)
                    a8.append(j)

                    #print("JAA",i)

                if int(t) in a8:
                    #print("Ja",a8)
                    #a7.append([ i[0],i[1] ] )
                    a7.append([ sys.argv[4], i[0],i[1],i[-1] ] )
                else:
                    next
        #next
                    ##a8 = [] 
                    #print("Ja",a7) 

                    #if a1 >= t and t <= a2:
                    ##if a1 >= t and t <= a2:
                         #print("Ja",i[0],a1,a2)
                         #a7.append([i[0],a1,a2])  
                    ##     a7.append([i[0],i[1]])  
                    ##else:
        #print("JA",a6,t)
                ##     next   
        #print("JA",a6,t)
        #print("JaA",a7[-1],t)
        #res = a7[-1]
        #print("JaaA", a7) 
except IndexError:
    #print("Provide search time -l 'Day Month day_of_the_month HH:MM:SS year'") 
    next


try:
    a5 = sys.argv[4]
    if len(a5) > 2 and a7 != []:
        print("Ja", a7)
    else:
        for i in a4_1:
            if i[1] == a5:
                #print("Ja", i)
                #if a7 != '':
                try:
                    print("Ja", i, res, a7)
                except NameError:
                    #else:
                    print("Ja", i, res)
except IndexError:
    for i in a4_1:
        print("Ja",i)
        #print("Ja",i[0], a_1[i[1]][0][0:2], a_3, a_1[i[1]][1], i[2]) 

    #print("Ja",a4)
    #print("Ja",a4_1)


    a3 = []
    a3_1 = int()
    a3_2 = int()

    cnt = 0

    #print("Ja",a2) 
    #sys.exit() 

    for i in a2:
        if i[2] != '0:0':
            ii = i[2].split(":")
            cnt += 1
            a3_1 += int(ii[0])
            a3_2 += int(ii[1])

    #print("Ja cnt", cnt)

    a3_3 = round(float(a3_2) / 60, 2)  
    a3_4 = str(a3_3).split(".")
    a3_5 = a3_1 + int(a3_4[0]) 

    a3_6 = '0.' + a3_4[1]
    a3_7 = round(float(a3_6) * 60)

    a3_8 = str(a3_5) + "." + str(a3_7)
    a3_9 = round(float(a3_8) / 12,2) 
    a3_10 = round(float(a3_9) / 4,2) 
    a3_11 = round(float(a3_8) / cnt,2)

    print("Uren ", c3, a3_8)
    print("Uren per maand ", c3, a3_9)
    #print("Gemiddeld aantal uur per week op basis van de gewerkte weken", "("+ str(cnt) + ")", c3, a3_11)
    print("Gemiddeld aantal uur per week op basis van de weken waarvoor sessie data beschikbaar is", "("+ str(cnt) + ")", c3, a3_11)
