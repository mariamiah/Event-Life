# Declare empty lists that shall contain names read from the files
ordinary_list = []
vip_list = []

# Read ordinary file and append names to a list
ordinary = open("ordinary.txt", "r")
ordinary_list = [line.rstrip() for line in ordinary.readlines()]


# Read VIP file and append names to the vip_list
vip = open("vip.txt", "r")
vip_list = [line.rstrip() for line in vip.readlines()]

# Request user to enter their name
singlename = input("Enter single name:")


def registration_checker_ordinary(singlename):
    ''' Function to check if a guest is registered
     in ordinary list '''
    return ''.join(name for name in ordinary_list if singlename in name) + ", ORDINARY"


def registration_checker_vip(singlename):
    ''' Function to check if a guest is registered
    in vip_list'''
    return ''.join(name for name in vip_list if singlename in name) + ", VIP"


def registration_checker(singlename):
    ''' Function that checks if the user exists either in ordinary_list
    or in vip_list'''
    if singlename in ordinary_list:
        return registration_checker_ordinary(singlename)
    elif singlename in vip_list:
        return registration_checker_vip(singlename)
    else:
        return "User not registered"
        
print(registration_checker(singlename))

ordinary.close()
vip.close()
