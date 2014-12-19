import sys
import csv

infile = sys.argv[1]
outfile = sys.argv[2]
if (infile == ""):
    print "need file name"
    exit()

with open(infile, 'rb') as f:
    reader = csv.reader(f)
    my_list = list(reader)
    print my_list

firstline = True 
headerlist = []
index = 0 
headerlength = 0
keyvaluelist = {}
#f = open('workfile', 'w')
f = open(outfile, 'w')
#print "lenth of list is: %s" % (len(my_list))
for mylist in my_list:
    if (firstline):
        firstline = False
        headerlist = mylist
        headerlength = len(headerlist)
        #print "this is the first header line: %s" % headerlist
        index = 0
        #for each header atrribute, make a new list
        for item in headerlist:
            keyvaluelist[index] = []
            index += 1
        continue
    index = 0
    for eachvalue in mylist:
        #print eachvalue
        #print "index at: %s" % index
        #get the existing list and add another value to it
        list1 = keyvaluelist[index]
        list1.append(eachvalue)
        keyvaluelist[index] = list1
        index += 1
index = 0
#write out the header and it's value within the list
for header in headerlist:
    #f.write(header+",")
    #f.write(keyvaluelist[index])
    print "header: %s" % header
    f.write(header+"|")
    for eachvalue in keyvaluelist[index]:
        #print "%s,%s" % (header, keyvaluelist[index])
        print "each value: %s" % eachvalue 
        f.write(eachvalue+"|")
    f.write("\n")
    index += 1
