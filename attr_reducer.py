#!/usr/bin/env python

from operator import itemgetter
import sys
import ast

current_key = None
key = None
mystring ='' 

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    keyvalue = line.split('|')
    key = keyvalue[0]
    nodistinct = keyvalue[1]
    noblank = keyvalue[2]
    totalcount = keyvalue[3]
    attrvalue = keyvalue[4]
    value = ast.literal_eval(keyvalue[4])
    attrvaluecount = ast.literal_eval(keyvalue[5])
    attrvaluecountstring = ""
    stringconcatlist = []
    missingpercent = round((float(noblank) / float(totalcount)),2)
    skewness = 0
    for k,v in attrvaluecount.iteritems():
        percentoftotal = round(v/float(totalcount),2)
        #print "percent of skewness for total count = %s with value=%s and total=%s is %s" % (totalcount,k,v,percentoftotal)
        if (percentoftotal > .75):
            skewness = 1
        stringconcatlist.append('%s,%s,%s|' % (str(k),str(v),str(percentoftotal)))
    #attrvaluecountstring += str(attrvaluecountstringtemp)
    attrvaluecountstring = ''.join(stringconcatlist)
   
    #for string in value:
    #mystring += string 
    mystring='|'.join(value)
    #attrvaluecounts='|'.join(attrvaluecount)
   
    # write for summary page 
    #print '1|attr=%s|distinct=%s|blanks=%s|missinperc=%s|skew=%s|' % (key,nodistinct,noblank,str(missingpercent),skewness)
    print '1|%s|%s|%s|%s|%s|' % (key,nodistinct,noblank,str(missingpercent),skewness)
    
    #write out for clean spreadsheet
    #print '%s|%s' % (key,attrvalue)
    print '2|%s|%s|' % (key,mystring)

    #write out for individual attribute sheet 
    print '3|%s|%s' % (key,attrvaluecountstring)
