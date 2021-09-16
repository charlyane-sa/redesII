from netaddr import *

ip = str(input('Digite o IP no formato xxx.xxx.xxx.xxx: ')).strip()

arqCSV = str(input('Informe o nome do arquivo CSV: ')).strip()
with open (arqCSV) as handle:
    for line in handle:
        ip_net, cidr, portaSaida = line.split(',')
        ip_net = ip_net.replace ("ï»¿","")
        ip_net = ip_net.strip()
        cidr = cidr.strip()
        portaSaida = portaSaida.strip()
        ipn_cidr = ip_net + '/' + cidr
        if IPAddress(ip) in IPNetwork (ipn_cidr):
            print(portaSaida)
        else: 
            print('Não localizado na tabela')
