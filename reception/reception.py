# Read ordinary file and append names to a list
ordinary = open("ordinary.txt", "r")
ordinary_list = [line.rstrip() for line in ordinary.readlines()]


# Read VIP file and append names to the vip_list
vip = open("vip.txt", "r")
vip_list = [line.rstrip() for line in vip.readlines()]

# Request user to enter their name
singlename = input("Enter single name:")


def registration_checker(singlename):
    ''' Function that checks if the user exists either in ordinary_list
    or in vip_list'''
    for name in ordinary_list:
        if name.split()[0] == singlename:
            return [name, "ORDINARY"]

    for name in vip_list:
        if name.split()[0] == singlename:
            return [name, "VIP"]
    
    for name in ordinary_list and vip_list:
        if singlename not in name.split()[0]:
            return "User does not exist"
print(registration_checker(singlename))

ordinary.close()
vip.close()
