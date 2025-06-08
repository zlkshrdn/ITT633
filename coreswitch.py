from netmiko import ConnectHandler

# Define the core switch configuration (adjust these details accordingly)
core_switch = {
    "device_type": "cisco_ios_telnet",  # Use 'cisco_ios' for SSH, 'cisco_ios_telnet' for Telnet
    "host": "192.168.206.129",  # Replace with your core switch's IP
    "port": 5006,  # Telnet port (adjust if using SSH)
}

# Configuration commands for the core switch
config_commands = [

    # Interface configurations for access ports
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

    # Trunk port configuration
    "interface f1/0",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan 1-2,10-40.1002-1005",

    # VLAN interface configurations (SVI)
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

    # Enable IP routing
    "ip routing",

    # OSPF configuration
    "router ospf 1",
    "network 192.168.10.0 0.0.0.255 area 0",
    "network 192.168.20.0 0.0.0.255 area 0",
    "network 192.168.30.0 0.0.0.255 area 0",
    "network 192.168.40.0 0.0.0.255 area 0",
    "exit"
]

# Connect to the core switch and apply the configurations
try:
    connection = ConnectHandler(**core_switch)
    connection.enable()  # Enter enable mode

    # Apply global configurations
    print("Applying global configurations...")
    config_output = connection.send_config_set(config_commands)
    print(config_output)

    # Run the "show vlan-switch brief" command to display VLAN information
    vlan_info_output = connection.send_command("show vlan-switch brief")
    print("VLAN Information:\n", vlan_info_output)

    # Run the "show trunk" command to display trunk port information
    trunk_info_output = connection.send_command("show trunk")
    print("Trunk Information:\n", trunk_info_output)

    connection.disconnect()
    print("Configuration applied successfully!")

except Exception as e:
    print(f"Failed to configure the core switch: {e}")
