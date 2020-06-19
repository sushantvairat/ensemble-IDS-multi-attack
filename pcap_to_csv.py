import sys
import multiprocessing 
import os 
import subprocess
import pandas as pd
from scapy.all import sniff  #packet sniffing library
from scapy.all import wrpcap #converting captured packet into pcap file library
import time
import datetime
import csv

pkt_pred=0

def worker1(i): #pcap file generationfunction
	
	pkt_list=sniff(timeout=20)
	print(pkt_list)	#print no. of packets capture
	filename="checktcp"+str(i)+".pcap"
	wrpcap(filename,pkt_list)


def worker2(i,t_end):  #pcap to csv function   #i gives you latest no. of csv file generating

	filename="attacks"+str(i)+".csv"	#name of csv of last set of packets created 
	pcap_filename="checktcp"+str(i)+".pcap" #name of pcap
	
	with open(filename,'w',newline='') as f: #blank csv file creation	
		w = csv.writer(f)
		w.writerow(cols)

	stri="(sudo ./kdd99extractor -e "+pcap_filename+" >> "+filename+")" #cmnd for running kddextractor on given pcap file to convert it into csv
	strl="(sudo ./kdd99extractor -e "+pcap_filename+" >> intermediate_log.csv)"	# same as above
	
	#sorting values in intermediate_log.csv 
	df=pd.read_csv("intermediate_log.csv")
	df.sort_values(by='timestamp', ascending=True, inplace =True) 
	#print(df)
	df.to_csv("intermediate_log.csv",index=False)

	#running kddextractor command
	tmp=subprocess.call(stri,shell=True)
	subprocess.call(strl,shell=True)

	global pkt_pred	#variable for getting predicted packet no.
	#print(pkt_pred)----
	#strlog="(sudo python3 packetlog.py "+str(global pkt_pred)+")"
	strlog=["sudo","python3","packetlog.py",str(pkt_pred)]
	f=subprocess.check_output(strlog)	#running packetlog and storing output
	pkt_pred=int(f.decode('utf-8'))

	df1=pd.read_csv("intermediate_log.csv").iloc[:pkt_pred,:]
	df2=pd.read_csv("templog.csv")
	result=pd.concat([df2,df1])
	result.to_csv("templog.csv",index=False)
	df1=pd.read_csv("intermediate_log.csv").iloc[pkt_pred:,:]
	df1.to_csv("intermediate_log.csv",index=False)
	




if __name__ == "__main__": 
	
	cols = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","source_ip","s_portno","destinaton_ip","d_portno","timestamp",'label',"Class",'Single/Multi']   #columns of final_log.csv file generated at end of prediction
	
	with open("final_log.csv",'w',newline='') as f: #creating blank final_log.csv
		w1 = csv.writer(f)
		w1.writerow(cols)
	cols = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","source_ip","s_portno","destinaton_ip","d_portno","timestamp"] ## columns of intermediate_log.csv
	with open("intermediate_log.csv",'w',newline='') as f: #creating blank intermediate_log.csv
		w1 = csv.writer(f)
		w1.writerow(cols)
	with open("templog.csv",'w',newline='') as f: #creating blank temp_log.csv
		w1 = csv.writer(f)
		w1.writerow(cols)
	
	i=1
	k=0
	from datetime import datetime # Current date time in local system 
	t_end = time.time() + 60 * 1         #setting the time of running the complete code for 1 minute
	o=subprocess.call("cd /sys/class/net/ | grep "" eth0/operstate",shell=True) # for checking ethernet connection is active or not
	#subprocess.call("(va=$(grep "" eth0/operstate)",spkt_predl=True)
	#print(o)
	if o==1: #if connection online
		pkt_list0=sniff(timeout=20) #packet sniffing for first v20 sec
		#print(pkt_list0)

		wrpcap('checktcp0.pcap',pkt_list0)
		
		while time.time()<t_end:	#for stopping the system after set no. of minutes here 1 min
			p1 = multiprocessing.Process(target=worker1, args=(i, )) 
			p2 = multiprocessing.Process(target=worker2, args=((i-1),(time.time()+15), )) 
			p2.start() #starting prediction of last pcap created 
			p1.start() #starting next packet generating
			p1.join() 
			p2.join()
			i+=1
		worker2(i-1,0)	#final prediction of remaining packets
		#t_end=time.time()+300 #if there are packets unpredicted uncomment these codes
		'''while time.time()<t_end:
			worker2(i-1,0)'''
