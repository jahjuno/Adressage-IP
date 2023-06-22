import re

print(''' 
            #########################################################################
            #                               ADRESSAGE IP                            #
            #########################################################################
''')

#retrieve values IP, Mask and number of subnetwork
net_ip_ad=input("Adresse Réseau :")

def verify_ip_ad(ad_ip):
    while not re.match("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ad_ip):
        ad_ip=input("Invalide IP\n Adresse Réseau:")
        list_v = ad_ip.split(".")
        conv_list = list(map(int, list_v))
        print(conv_list)
        for i in range(len(conv_list)):
            if conv_list[i] > 255 :
                print("error")
                ad_ip=input("Invalide IP\n Adresse Réseau:")
        print("Adresse réseau : ", ad_ip)  

   
verify_ip_ad(net_ip_ad)


net_mask = input("Masque : ")
while not re.match(r"^2{1}55\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", net_mask):
    net_mask = input("Invalide Masque\n Masque : ")

subnet_number = int(input("Nombre de sous-réseau :"))
i=0
while i < subnet_number:
    print("Sous-réseau n°",i+1)
    npc_number = input("Nombre de machine:")
    i = i + 1
#End__retrieve values IP and Mask

