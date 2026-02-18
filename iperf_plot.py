import pandas as pd
import matplotlib.pyplot as py

#read the tcp and udp files
#CHANGE the 2m for distance
tcp = pd.read_csv('iperf_tcp_4m.csv')
udp = pd.read_csv('iperf_udp_4m.csv')

#get a list of the runs
run = ['Run1', 'Run2', 'Run3', 'Run4', 'Run5']

#fill the data variable with the last row of the csv
tcpData = tcp[run].iloc[-1]
udpData = udp[run].iloc[-1]

#plot run vs the data
py.plot(run, tcpData, color = 'red', label = 'TCP Throughput (Mbps)')
py.plot(run, udpData, color = 'blue', label = 'UDP Throughput (Mbps)')

#CHANGE the title
py.title("TCP & UDP Throughput at 4m Distance")
py.xlabel("Test Runs")
py.ylabel("Throughput (mbps)")
py.legend()

py.savefig('signal_4m.png')

#To send to rpi scp /home/alan/Desktop/lab5/iperf_plot.py pi@-------:~/
#To pull image from rpi scp pi@------:~/signal_2m.png ~/Deesktop/

