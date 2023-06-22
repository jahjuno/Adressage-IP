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
           

   
verify_ip_ad(net_ip_ad)