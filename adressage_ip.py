import re

print(''' 
            #########################################################################
            #                               ADRESSAGE IP                            #
            #########################################################################
''')

#retrieve values IP

net_ip_ad, i = '', 0
while not re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', net_ip_ad):
    net_ip_ad = input("Entrez l'addresse réseau >>>  "
        if i == 0 else "Invalide IP \nEntrez l'addresse réseau >>> ")
    i += 1

#retrieve Network Mask 
subnet_mask,y= '', 0
while not re.match(r'2{1}55.\d{1,3}.\d{1,3}.\d{1,3}$', subnet_mask):
    subnet_mask = input("Entrez le masque >> "
        if y == 0 else "Invalide Masque \n Entrez le masque >>")
    y += 1
    # Convertion mask notation to CIDR notation
    mask_list = {
        '255.0.0.0': '/8', '255.128.0.0': '/9', '255.192.0.0': '/10', '255.224.0.0': '/11', '255.240.0.0': '/12', '255.248.0.0': '/13', '255.252.0.0': '/14', '255.254.0.0': '/15', '255.255.0.0': '/16', 
        '255.255.128.0': '/17', '255.255.192.0': '/18', '255.255.224.0': '/19', '255.255.240.0': '/20', '255.255.248.0': '/21', '255.255.252.0': '/22', '255.255.254.0': '/23', '255.255.255.0': '/24',
        '255.255.255.128': '/25', '255.255.255.192': '/26', '255.255.255.224': '/27', '255.255.255.240': '/28', '255.255.255.248': '/29', '255.255.255.252': '/30', '255.255.255.254': '/31', '255.255.255.255': '/32'
    }

    if subnet_mask in mask_list.keys():
        element = mask_list[subnet_mask]

        print(net_ip_ad + element)


#retrieve Number of subnet 
nb_subnet = ''
i = 0
while not re.match(r'\d+$', nb_subnet):
    nb_subnet = input("\nEntrez le nombre de sous réseau >>> "
        if i == 0 else "Ecrivez un nombre !!! \nEntrer le nombre de sous réseau >>> ")
    i += 1
    a=0
    while a < int(nb_subnet) : 
        nb_pc = input("Entrez nombre de machine sous-réseau>>>")
        a+=1



