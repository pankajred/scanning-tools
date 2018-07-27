#!/usr/bin/python2	
import os
import commands
import time
import thread

commands.getoutput("rm -rf /root/ip_working")
commands.getoutput("rm -rf /root/ip_not_working")
os.system('tput setaf 2')
print "\t\t\t\tWELCOME TO IP SCANNING TOOL"
time.sleep(2)
print "\n"
os.system('tput setaf 4')
print "\t\t\t\tListing Your Active network cards name"
time.sleep(3)

#len_card=commands.getoutput('tcpdump -D')
len_card=commands.getoutput('ifconfig | cut -c1-8 | sort -u')
print (len_card)
print ("\t\t\t\t----------------------------------------------------")
print "\n"
time.sleep(1)
os.system('tput setaf 5')


print ("\t\t\t\tType your network card name")
lencard=raw_input() 

if lencard in len_card:
	print "Card Selected "

else:
	print "Wrong network card name"
	time.sleep(1)
	print "\n"
	print "you have typed wrong network card name"
	time.sleep(3)
	print "Restarting your program ...."
	time.sleep(1)
	print "Restarting your program ......."
	execfile('nmap.py')

r=commands.getoutput("ifconfig {0}".format(lencard))
y=r.split('inet')[1]
ip=y.split()[0]

q=ip.split('.')
ip1=[]
for i in q[0:3]:
	ip1.append(i)


ip2=".".join(str(x) for x in ip1)
	 
time.sleep(2)
print ("\t\t\t\tyour ip is {}".format(ip))
os.system('tput setaf 3')
print ("\t\t\t\tscanning is starting with this ip({0})".format(ip))

try:

	print "\t\t\t\tScanning is starting "

	def a():

		for i in range(100,116):
			y=commands.getstatusoutput('ping -i 0.1 -c 1 {0}.{1}'.format(ip2,i))
			if y[0] == 0:
				print "-------------------"
				q=y[1].split()
				print q[1]
				print "ip is working"
				fh=open('/root/ip_working','a')
				fh.write(q[1])
				fh.write('\n')
				fh.close()
		
		
			else:
 				print "--------------------"
				q=y[1].split()
				print q[1]
				print "ip is not working"
				ff=open('/root/ip_not_working','a')
				ff.write(q[1])
				ff.write('\n')
				ff.close	


	def b():

        	for i in range(116,130):
                	y=commands.getstatusoutput('ping -i 0.1 -c 1 {0}.{1}'.format(ip2,i))
                	if y[0] == 0:
                        	print "-------------------"
                        	q=y[1].split()
				print q[1]
				print "ip is working"
                        	fh=open('/root/ip_working','a')
				fh.write(q[1])
				fh.write('\n')
        	                fh.close()
	

                	else:
                        	print "--------------------"
                        	q=y[1].split()
				print q[1]
				print "ip is not working"
				ff=open('/root/ip_not_working','a')
                     		ff.write(q[1])
				ff.write('\n')
                        	ff.close

	def c():

                for i in range(130,151):
                        y=commands.getstatusoutput('ping -i 0.1 -c 1 {0}.{1}'.format(ip2,i))
                        if y[0] == 0:
                                print "-------------------"
                                q=y[1].split()
                                print q[1]
                                print "ip is working"
                                fh=open('/root/ip_working','a')
                                fh.write(q[1])
                                fh.write('\n')
                                fh.close()


                        else:
                                print "--------------------"
                                q=y[1].split()
                                print q[1]
                                print "ip is not working"
                                ff=open('/root/ip_not_working','a')
                                ff.write(q[1])
                                ff.write('\n')
                                ff.close



	thread.start_new_thread( a,( ) )
	thread.start_new_thread( b,( ) )
	thread.start_new_thread( c,( ) )

	input('Presss Enter to stop')	
	time.sleep(3)
	commands.getoutput('tput setaf 2')
	print "your both files is ready check it now ..!!"

except	SyntaxError:
	print "Task completed ...!"
	
