import pexpect
import os
import re
import sys
from subprocess import Popen, PIPE

def exec_cmd(cmd):
    print ("** Running cmd : {}".format(cmd))
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    print ("#### output : {0} and error : {1}".format(output, err))
    return output, err
    
timeout=120
linux_prompt = re.compile(r':~#', re.M)
connect_errors = re.compile('ermission denied', re.M)
ssh_pass = re.compile(r'^.*password:\s$', re.M | re.IGNORECASE)
known_errors = 'ssh:denied|No route|not resolve host|refused'
expReturns = [ssh_pass, linux_prompt, pexpect.TIMEOUT, pexpect.EOF, known_errors, connect_errors]
ssh_cmd = ("ssh -o StrictHostKeyChecking=no -o "
               "UserKnownHostsFile=/dev/null %s@%s" % ('root', '10.33.0.141'))
session = pexpect.spawn(ssh_cmd, timeout=timeout)
#session.logfile_read = sys.stdout
remoteLogin = False
runMysqlCmd = False
while True:
    ret = session.expect(expReturns, timeout=timeout)
    #print (ret)
    if ret == 0:
        if not remoteLogin:
            session.sendline('Gone2far123\$')
            remoteLogin=True
        else:
            session.sendline('SOP2tfIm7C20sYNT')
        continue
    if ret == 1:
        if not runMysqlCmd:
            print ('** Successfully login to remote server - 141')
            remoteLogin=True
            mysqlCmd = 'mysqldump -u hxqa -p -h hx-db.cisco.com --ssl-ca=ca.pem --ssl-cert=client-cert.pem --ssl-key=client-key.pem qa > /builds/utils/time_db_dump.sql'
            print ('** Running cmd : {}'.format(mysqlCmd))
            session.sendline(mysqlCmd)
            runMysqlCmd=True
        else:
            print ("** Successfully dumped the mysql 'qa' data..!!")
            print ("** Changing ENGINE, CHARSET and COLLATE")
            changeCmd = 'sed -i "s/ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci/ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci/g" /builds/utils/time_db_dump.sql'
            session.sendline(changeCmd)
            session.expect(linux_prompt, timeout=timeout)
            session.close(force=True)
            break
    if ret in (2, 3, 4, 5):
        # EOF
        print ("** Unexpected disconnection, ret : {}".format(ret))
        session.close(force=True)
        break
    
print ('** Reloading remote mysql dump to local DB')
exec_cmd('mysql qa < /builds/utils/time_db_dump.sql')
