from netmiko import ConnectHandler

# Define the router configuration (adjust these details accordingly)
router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.206.129",  # Replace with the IP address of Router-HQ
    "port": 5074,  # Default SSH port
}

# Configuration commands for Router-HQ
config_commands = [
    "interface s1/0",
    "ip address 10.10.10.2 255.255.255.0",
    "no shutdown",
    "exit",
    "router ospf 1",
    "router-id 1.1.1.1",  # Assign a unique router ID for Router HQ
    "network 192.168.10.0 0.0.0.255 area 0",
    "network 192.168.20.0 0.0.0.255 area 0",
    "network 192.168.30.0 0.0.0.255 area 0",
    "network 192.168.40.0 0.0.0.255 area 0",
    "exit",
    "ip route 10.10.10.0 255.255.255.0 10.10.10.1"
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
