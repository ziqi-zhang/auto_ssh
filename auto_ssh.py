import pexpect
import argparse

IPs = {
IP_alias_1: IP_1,
IP_alias_2: IP_2
}

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", required=True, choices = IPs.keys())
args = parser.parse_args()
print(args.server)
server = args.server
ip = IPs[server]
user = "your username"
passwd = "your password"
mid_server_ip = "middle server ip"
child = pexpect.spawn('ssh %s@%s'%(user, mid_server_ip))
child.expect('Respond of middle server')
child.sendline(passwd)
child.expect('Respond about the server you are going to login')
child.sendline(ip)
child.interact()
