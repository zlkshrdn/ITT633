from netmiko import ConnectHandler

# Device configurations (replace with actual switch management IPs)
switch = {
    "device_type": "cisco_ios_telnet",  # Use cisco_ios_telnet for Telnet
    "host": "192.168.206.129",  # Router IP
    "port": 5013,  # Telnet port
}

# IP configurations for VPCs
vpcs_config = {
    "VLAN30": [
        {"interface": "e1", "ip": "192.168.30.3", "subnet": "255.255.255.0", "gateway": "192.168.30.1"},
        {"interface": "e2", "ip": "192.168.30.4", "subnet": "255.255.255.0", "gateway": "192.168.30.1"},
        {"interface": "e3", "ip": "192.168.30.5", "subnet": "255.255.255.0", "gateway": "192.168.30.1"},
        {"interface": "e4", "ip": "192.168.30.6", "subnet": "255.255.255.0", "gateway": "192.168.30.1"},
        {"interface": "e5", "ip": "192.168.30.7", "subnet": "255.255.255.0", "gateway": "192.168.30.1"},
    ],
}

# Generate commands for each VLAN
def generate_ip_config_commands(vpcs):
    commands = []
    for vlan, interfaces in vpcs.items():
        for interface in interfaces:
            commands.append(f"interface {interface['interface']}")
            commands.append(f"ip address {interface['ip']} {interface['subnet']}")
            commands.append("no shutdown")
    return commands

# Function to configure the switch
def configure_device(device, commands):
    try:
        connection = ConnectHandler(**device)
        print(f"Connecting to {device['host']}...")
        output = connection.send_config_set(commands)
        print(output)
        connection.disconnect()
    except Exception as e:
        print(f"Failed to configure {device['host']}: {e}")

# Generate IP configuration commands
ip_config_commands = generate_ip_config_commands(vpcs_config)

# Apply IP configurations to the Core Switch
configure_device(switch, ip_config_commands)
