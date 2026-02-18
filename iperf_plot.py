import pandas as pd
import matplotlib.pyplot as py

#read the tcp and udp files
tcp = pd.read_csv('iperf_tcp_2m.csv')
udp = pd.read_csv('iperf_udp_2m.csv')
tcp2 = pd.read_csv('iperf_tcp_6m.csv')
udp2 = pd.read_csv('iperf_udp_6m.csv')
tcp3 = pd.read_csv('iperf_tcp_8m.csv')
udp3 = pd.read_csv('iperf_udp_8m.csv')
tcp4 = pd.read_csv('iperf_tcp_10m.csv')
udp4 = pd.read_csv('iperf_udp_10m.csv')
tcp5 = pd.read_csv('iperf_tcp_12m.csv')
udp5 = pd.read_csv('iperf_udp_12m.csv')


#get a list of the runs
run = ['Run1', 'Run2', 'Run3', 'Run4', 'Run5']
distances = ['4', '6', '8', '10', '12']
tcpData = []
udpData = []

#fill the data variable with the last row of the csv
tcpData.append(tcp['Avg'].iloc[-1])
udpData.append(udp['Avg'].iloc[-1])
tcpData.append(tcp2['Avg'].iloc[-1])
udpData.append(udp2['Avg'].iloc[-1])
tcpData.append(tcp3['Avg'].iloc[-1])
udpData.append(udp3['Avg'].iloc[-1])
tcpData.append(tcp4['Avg'].iloc[-1])
udpData.append(udp4['Avg'].iloc[-1])
tcpData.append(tcp5['Avg'].iloc[-1])
udpData.append(udp5['Avg'].iloc[-1])



#plot run vs the data
py.plot(distances, tcpData, color = 'red', label = 'TCP Throughput (Mbps)')
py.plot(distances, udpData, color = 'blue', label = 'UDP Throughput (Mbps)')

#CHANGE the title
py.title("Average TCP & UDP Throughput at Each Distance")
py.xlabel("Distances")
py.ylabel("Throughput (mbps)")
py.legend()

py.savefig('averageTCP.png')

#To send to rpi scp /home/alan/Desktop/lab5/iperf_plot.py pi@-------:~/
#To pull image from rpi scp pi@------:~/signal_2m.png ~/Deesktop/

