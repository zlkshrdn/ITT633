from netmiko import ConnectHandler

# Define the router configuration (adjust these details accordingly)
router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.206.129",  # Replace with your router's IP
    "port": 5072 # SSH port (default is 22)
}

# Configuration commands for the router
config_commands = [
    "interface f0/0",
    "no shutdown",

    "interface f0/0.10",
    "encapsulation dot1Q 10",
    "ip address 192.168.10.1 255.255.255.0",

    "interface f0/0.20",
    "encapsulation dot1Q 20",
    "ip address 192.168.20.1 255.255.255.0",

    "interface f0/0.30",
    "encapsulation dot1Q 30",
    "ip address 192.168.30.1 255.255.255.0",

    "interface f0/0.40",
    "encapsulation dot1Q 40",
    "ip address 192.168.40.1 255.255.255.0",

    "interface f0/0.99",
    "encapsulation dot1Q 99",
    "ip address 192.168.99.1 255.255.255.0",
    "exit",

    "router ospf 1",
    "router-id 1.1.1.1",
    "network 192.168.10.0 0.0.0.255 area 0",
    "network 192.168.20.0 0.0.0.255 area 0",
    "network 192.168.30.0 0.0.0.255 area 0",
    "network 192.168.40.0 0.0.0.255 area 0",

    'interface s1/0',
    'ip address 10.10.10.1 255.255.255.0',
    "no shutdown",
    "exit",
    'ip route 10.10.10.0 255.255.255.0 10.10.10.2',
    "end",

]

# Connect to the router and apply the configurations
try:
    connection = ConnectHandler(**router)
    connection.enable()  # Enter enable mode

    print("Applying configurations...")
    output = connection.send_config_set(config_commands)
    print(output)

    # Save configuration to memory
    print("Saving configuration to memory...")
    output = connection.send_command("write memory")
    print(output)

    connection.disconnect()
    print("Configuration applied successfully!")

except Exception as e:
    print(f"Failed to configure the router: {e}")
