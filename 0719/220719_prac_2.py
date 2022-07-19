ports = [False]*15
ports[3] = True
ports[7] = True
ports[8] = True
ports[14] = True
print(ports)

odd_ports = []
for i in range(len(ports)):
    if i%2 == 0:
        odd_ports.append(ports[i])
print(odd_ports)