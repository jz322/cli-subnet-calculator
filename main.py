import sys

# this function will verify the given IP address and Subnet mask to make sure they fit the criteria
def formatAddresses(ip, subnet):
    # these variables will store the verified IP address and subnet mask
    formatted_ip = []
    formatted_subnet = []

    subnet_full = subnet.split('.')
    ip_address = ip.split('.')

    # checks that the address and lenght both include 4 octets
    if len(ip_address) < 4:
        print("Invalid IP address, format should be x.x.x.x and each octet should be in the range 0-255")
        return
    elif len(subnet_full) < 4:
        print("Invalid Subnet mask, format should be x.x.x.x and each octet should be in the range 0-255")
        return

    # checks each octet that the decimal value is in the correct range (from all 0s in binary to all 1s)
    for i in range (0, 4):
        if (int(ip_address[i]) >= 0) and (int(ip_address[i]) <= 255):
            formatted_ip.append(int(ip_address[i]))
        else:
            print(f"Invalid IP address octet number {i}: {ip_address[i]}\nValid range is 0-255")

    for i in range (0, 4):
            if (int(subnet_full[i]) >= 0) and (int(subnet_full[i]) <= 255):
                formatted_subnet.append(int(subnet_full[i]))
            else:
                print(f"Invalid Subnet mask octet number {i}: {subnet_full[i]}\nValid range is 0-255")
    print(formatted_ip)
    print(formatted_subnet)


def calculateSubnet(ip, subnet):
    print("nothing yet")

if __name__ == "__main__":
    print("Subnet Calculator v1.0\n")

    ipv4 = input("Enter the IP address: ")
    subnet = input("Enter the subnet mask: ")

    formatAddresses(ipv4, subnet)