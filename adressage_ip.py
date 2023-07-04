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
    mask_list = ["255.0.0.0", "255.128.0.0", "255.192.0.0", "255.224.0.0", "255.240.0.0", "255.248.0.0", "255.252.0.0", "255.254.0.0",
                 "255.255.0.0", "255.255.128.0", "255.255.192.0", "255.255.224.0","255.255.240.0", "255.255.248.0", "255.255.252.0", "255.255.254.0",
                 "255.255.255.0", "255.255.255.128", "255.255.255.192", "255.255.255.224", "255.255.255.240", "255.255.255.248", "255.255.255.252", "255.255.255.254", "255.255.255.255"
                 ]
    cidr_mask__list = ["/8", "/9", "/10", "/11", "/12", "/13", "/14", "/15", "/16", "/17", "/18", "/19", "/20", "/21", "/22",
                       "/23", "/24", "/25", "/26", "/27", "/28", "/29", "/30", "31", "32"
                       ]
    if subnet_mask in mask_list:
        index = mask_list.index(subnet_mask)
        element = cidr_mask__list[index]

        print(subnet_mask, element)


#retrieve Number of subnet 
nb_subnet = ''
i = 0
while not re.match(r'\d+$', nb_subnet):
    nb_subnet = input("\nEntrez le nombre de sous réseau >>> "
        if i == 0 else "Ecrivez un nombre !!! \nEntrer le nombre de sous réseau >>> ")
    i += 1




