import re

print(''' 
            #########################################################################
            #                               ADRESSAGE IP                            #
            #########################################################################
''')

#retrieve values IP

def validate_ip(ip_adresse): 
    regex_ip = r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$'
    if not re.match(regex_ip, ip_adresse):
        return False
    try:
        conv_ip_add = ip_adresse.split(".")
        for element in conv_ip_add:
            ipd = int(element)
            if ipd>255:
                return False
    except ValueError:
        return False
    
    return True

def check_ip():
    ip_address = input("Entrez l'addresse réseau >>>  ")
    while not validate_ip(ip_address):
       ip_address = input("Invalide IP \nEntrez l'addresse réseau >>>  ")
    print("Adresse Réseau: ",ip_address) 

check_ip()


def validate_mask(mask_add):
    regex_mask = r'2{1}55.\d{1,3}.\d{1,3}.\d{1,3}$'
    if not re.match(regex_mask, mask_add):
        return False
    try:
        conv_mask = mask_add.split(".")
        for element in conv_mask:
            mask = int(element)
            if mask > 255:
                return False
    except ValueError:
        return False
    return True

def mask_recup():
    mask_add = input("Entrez le masque >>  ")
    while not validate_ip(mask_add):
       mask_add = input("Invalide Masque \nEntrez le masque >>  ")

    mask_list = {
        '255.0.0.0': '/8', '255.128.0.0': '/9', '255.192.0.0': '/10', '255.224.0.0': '/11', '255.240.0.0': '/12', '255.248.0.0': '/13', '255.252.0.0': '/14', '255.254.0.0': '/15', '255.255.0.0': '/16', 
        '255.255.128.0': '/17', '255.255.192.0': '/18', '255.255.224.0': '/19', '255.255.240.0': '/20', '255.255.248.0': '/21', '255.255.252.0': '/22', '255.255.254.0': '/23', '255.255.255.0': '/24',
        '255.255.255.128': '/25', '255.255.255.192': '/26', '255.255.255.224': '/27', '255.255.255.240': '/28', '255.255.255.248': '/29', '255.255.255.252': '/30', '255.255.255.254': '/31', '255.255.255.255': '/32'
    }
    if mask_add in mask_list.keys():
        element = mask_list[mask_add]

        print(element, "\n("+"Masque : ", mask_add+")")
    else : 
        print("Masque :"+mask_add)
 

mask_recup()

#retrieve Number of subnet 
nb_subnet = ''
i = 0
while not re.match(r'\d+$', nb_subnet):
    nb_subnet = input("\nEntrez le nombre de sous réseau >>> "
        if i == 0 else "Ecrivez un nombre !!! \nEntrer le nombre de sous réseau >>> ")
    i += 1


