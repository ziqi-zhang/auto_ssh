import pexpect
import argparse

IPs = {
"bj15": "10.10.15.115",
"bj17": "10.10.17.21",
"sh30": "10.5.30.231",
"office": "10.1.12.75"
}

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", required=True, choices = IPs.keys())
args = parser.parse_args()
print(args.server)
server = args.server
ip = IPs[server]
if server!="office":
    user = "zhangziqi"
    passwd = "Goodsense@"
    mid_server_ip = "10.10.10.27"
    child = pexpect.spawn('ssh %s@%s'%(user, mid_server_ip))
    child.expect('zhangziqi@10.10.10.27\'s password:')
    child.sendline(passwd)
    child.expect('zhangziqi Please enter your Login Ip:')
    child.sendline(ip)
    child.interact()
else:
    user = "\"SENSETIME\zhangziqi\""
    passwd = "Goodsense@"
    child = pexpect.spawn('ssh %s@%s'%(user, ip))
    child.expect('Password:')
    child.sendline(passwd)
    child.interact()
