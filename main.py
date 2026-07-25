import sys

# this function will verify the given IP address and Subnet mask to make sure they fit the criteria
def formatAddresses(ip, subnet):
    formated_ip = []
    ip_address = ip.split('.')
    if len(ip_address) < 4:
        print("Invalid address, format should be x.x.x.x and each octet should be in the range 0-255")
        return
    for i in range (0, 4):
        if (ip_address[i] >= 0) and (ip_address[i] <= 255):
            formated_ip.append(int(ip_address[i]))
        else:
            print(f"Invalid Octet number")

    subnet_full = subnet.split('.')
    sub_oct1 = int(subnet_full[0])
    sub_oct2 = int(subnet_full[1])
    sub_oct3 = int(subnet_full[2])
    sub_oct4 = int(subnet_full[3])


        

if __name__ == "__main__":
    print("Subnet Calculator v1.0")