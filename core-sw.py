from netmiko import ConnectHandler

# Define the switch configuration (adjust these details accordingly)
switch = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.206.129",
    "port": 5036,
}

# VLAN database commands (outside of configure terminal)
vlan_commands = [
    "vlan database",
    "vlan 10 name Server",
    "vlan 20 name Sale",
    "vlan 30 name Marketing",
    "vlan 40 name Management",
    "apply",
    "abort"
]

# Main configuration commands (inside configure terminal)
main_config_commands = [
    "conf t",
    "interface f1/1",
    "switchport mode access",
    "switchport access vlan 10",
    "interface f1/2",
    "switchport mode access",
    "switchport access vlan 20",
    "interface f1/3",
    "switchport mode access",
    "switchport access vlan 30",
    "interface f1/4",
    "switchport mode access",
    "switchport access vlan 40",
    "interface f1/0",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk native vlan 99",
    "switchport trunk allowed vlan 1-2,10-40.1002-1005",
    "interface vlan 10",
    "ip address 192.168.10.2 255.255.255.0",
    "no shutdown",
    "interface vlan 20",
    "ip address 192.168.20.2 255.255.255.0",
    "no shutdown",
    "interface vlan 30",
    "ip address 192.168.30.2 255.255.255.0",
    "no shutdown",
    "interface vlan 40",
    "ip address 192.168.40.2 255.255.255.0",
    "no shutdown",
    "ip routing",
    "router ospf 1",
    "network 192.168.10.0 0.0.0.255 area 0",
    "network 192.168.20.0 0.0.0.255 area 0",
    "network 192.168.30.0 0.0.0.255 area 0",
    "network 192.168.40.0 0.0.0.255 area 0",
    "network 192.168.99.0 0.0.0.255 area 0",
    "exit"
]

# Connect to the switch and apply the VLAN and main configuration commands
try:
    # Establish the SSH connection
    connection = ConnectHandler(**switch)

    # Apply VLAN database commands
    print("Applying VLAN database configurations...")
    output = connection.send_config_set(vlan_commands)
    print(output)

    # Apply main configuration commands
    print("Applying main configurations...")
    output = connection.send_config_set(main_config_commands)
    print(output)

    # Save configuration to memory
    print("Saving configuration to memory...")
    output = connection.send_command("write memory")
    print(output)

    connection.disconnect()  # Disconnect from the switch
    print("Configuration applied successfully!")

except Exception as e:
    print(f"Failed to configure the switch: {e}")
