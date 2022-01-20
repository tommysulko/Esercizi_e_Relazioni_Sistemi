ip_address = ["192.168.11.0/24","192.168.11.0/30","192.168.11.0/14","192.168.11.0/27"]

f = open("./provaVerifica","w")

for ip in ip_address:
    f.write(ip[:-3])
    f.write(" ")
f.close()



