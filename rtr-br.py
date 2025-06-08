from netmiko import ConnectHandler

# Router connection details
router = {
    "device_type": "cisco_ios_telnet",  # Use cisco_ios_telnet for Telnet
    "host": "192.168.206.129",  # Router IP
    "port": 5072,  # Telnet port
}

# Commands to configure the router (hostname)
config_commands = [
    "configure terminal",  # Enter global configuration mode
    "hostname Router-Branch",  # Set hostname
    "end",  # Exit global configuration mode
    "write memory"  # Save the configuration
]


# Function to configure the router's hostname
def configure_hostname(connection):
    try:
        # Send hostname configuration commands
        print("Configuring hostname...")
        output = connection.send_config_set(config_commands)
        print(output)
    except Exception as e:
        print(f"An error occurred while configuring hostname: {e}")

# Function to show IP interfaces brief
def show_ip_int_br(connection):
    try:
        # Run show IP interface brief command to display the IP interfaces
        print("Displaying IP Interface Brief...")
        output = connection.send_command("show ip int br")
        print("IP Interface Brief:")
        print(output)
    except Exception as e:
        print(f"An error occurred while displaying IP interface brief: {e}")


# Function to show OSPF routes
def show_ospf_routes(connection):
    try:
        # Run show IP route OSPF command to display OSPF routes
        print("Displaying OSPF routes...")
        output = connection.send_command("show ip ospf route")
        print("OSPF Routes:")
        print(output)
    except Exception as e:
        print(f"An error occurred while displaying OSPF routes: {e}")



# Function to show OSPF neighbors
def show_ospf_neighbors(connection):
    try:
        # Run show IP OSPF neighbor command to display OSPF neighbors
        print("Displaying OSPF neighbors...")
        output = connection.send_command("show ip ospf neighbor")
        print("OSPF Neighbors:")
        print(output)
    except Exception as e:
        print(f"An error occurred while displaying OSPF neighbors: {e}")


# Main function to execute all tasks
def main():
    try:
        # Connect to the router
        print("Connecting to the router...")
        connection = ConnectHandler(**router)

        # Enter enable mode if required
        if not connection.check_enable_mode():
            connection.enable()

        # Execute the tasks sequentially
        configure_hostname(connection)  # Configure hostname
        show_ip_int_br(connection)  # Show IP interface brief
        show_ospf_routes(connection)  # Show OSPF routes
        show_ospf_neighbors(connection)  # Show OSPF neighbors

        # Disconnect from the router
        connection.disconnect()
        print("All tasks completed. Connection closed.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
