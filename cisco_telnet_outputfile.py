from netmiko.ssh_dispatcher import ConnectHandler
from datetime import datetime

start_time = datetime.now() 
print(start_time)

connection = ConnectHandler(host='11.11.11.11',
                            username='cisco',
                            password='cisco123',
                            device_type='cisco_ios_telnet'
                            )

connection = ConnectHandler(**test1)

print("--------- Start : ConnectHandler['host']---------")

connection.disable_paging()

connection.enable()
output = connection.send_command(command_string='show run')
print(output)

connection.disconnect()


print("--------- End ---------")

end_time = datetime.now() 
print(end_time)
total_time = end_time - start_time 
print(total_time)


saveoutput = open("backup-file" + start_time.strftime('%Y%m%d_%H%M'), 'w')
saveoutput.write(output.decode)
saveoutput.write("\n")
saveoutput.close