import os, sys

def kill(process = 'crclient'):
    for proc in os.popen('ps -A | grep ' + str(process)).read().split('\n'):
        pdata = proc.split()
        pid = int(pdata[0]) if pdata else -1
        if pid == -1:
            continue
        os.system('kill -9 ' + str(pid))

def on(user='rishi_cse36_2010'):
    kill()
    os.popen('rm -rf /tmp/crclient.pid')
    os.chdir('CyberoamLinuxClient')
    pout = os.popen('./crclient -u rishi_cse36_2010').read()

def off(user='rishi_cse36_2010'):
    kill()
    os.popen('rm -rf /tmp/crclient.pid')
    os.chdir('CyberoamLinuxClient')
    pout = os.popen('./crclient -l').read()
    if 'Not' in pout:
        print "Logged out."
    else:
        print "Error Occurred in logging out."

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Enter 0 for logout and 1 for login."
        sys.exit()
    option = sys.argv[1]
    if option == '1':
        on()
    else:
        off()