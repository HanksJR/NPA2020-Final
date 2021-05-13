from netmiko import ConnectHandler

def main():
    device_ip = "10.0.15.118"
    username = "admin"
    password = "cisco"
    command = ["int loopback 61070266", "ip address 192.168.1.1 255.255.255.0"]
    device_params = {'device_type': 'cisco_ios',
                        'ip': device_ip,
                        'username': username,
                        'password': password,
                    }
    with ConnectHandler(**device_params) as ssh:
        ssh.send_config_set(command)

main()