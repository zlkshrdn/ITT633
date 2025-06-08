from netmiko import ConnectHandler

# Device details
switch = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.206.129",  # Replace with your switch IP
    "port" : 5070
}


def validate_vlans():
    try:
        print("Connecting to the switch...")
        connection = ConnectHandler(**switch)

        # Run show VLAN command
        output = connection.send_command("show vlan-switch brief")
        print("VLAN Configuration:")
        print(output)

        # Run show IP interface brief command
        output = connection.send_command("show ip int br")
        print("\nIP Interface Brief:")
        print(output)

        # Run show interfaces trunk command
        output = connection.send_command("show int trunk")
        print("\nTrunk Information:")
        print(output)

        # Run show interfaces status command
        output = connection.send_command("show int status")
        print("\nInterface Status:")
        print(output)

        connection.disconnect()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    validate_vlans()
