from datetime import datetime
from dateutil import parser
import sys


#git gave me an error message,when I tried to submit problem1,
#talking about some CONFLIT issue,
#so I googled it, and was suggested a hard reset.
#Then I lost my  file, if this doesn't run,
#I don't care anymore, since I didn't learn anything in class.
#The worst part is, the lost problem1.py was the only one that ran in my fold!
#FML

outputfile=[]#the final list shouldbe stored here

deadline=sys.argv[1]#read the give date and time as the deadline
 
deadline_time= parser.parse(deadline)#convert the time string to
#actual time with parse trick

log_file=open("logAfterAssignment1.txt","r")
#need to find "date:"from the log file


commit_time=[]#store all the commit time in this list
for line in log_file:
    committime=line.find("Date:")#if the line start with these five characters, we read its content
    if committime!=-1:
        for i in range(len(committime)):#label all the lines, and
            
            commit_time=parser.parse(log_file[i][8:-6])#ignoring the timezone info here
        if commit_time > deadline_time:
            output_file=outputfile.append()

log_file.close()
    



