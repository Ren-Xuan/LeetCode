import os
import time
import subprocess
import argparse
 
class TimeoutError(Exception):
    pass 

def excuteCmd(local,repos, timeout = 2):
        s = subprocess.Popen("C:\Windows\System32\cmd.exe",stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell = True)
        time.sleep(timeout)
        s.stdin.write(str.encode('git init \n'))
        time.sleep(timeout)
        s.stdin.write(str.encode('git add . \n'))
        time.sleep(timeout)
        s.stdin.write(str.encode('git remote add '+repos+"\n"))
        time.sleep(timeout)
        s.stdin.write(str.encode('git commit -m \"'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  +"\"\n"))
        time.sleep(timeout)
        s.stdin.write(str.encode('git push origin master\n'))
        time.sleep(timeout)
        out, err =s.communicate(str.encode('yes\n'))
        print(out.decode(encoding='gbk'))
        time.sleep(timeout)
        s.kill()
    
 
if __name__ == '__main__':
        ''' self test ''' 
        parser = argparse.ArgumentParser(description='manual to this script')
        parser.add_argument('--local', type=str,default=None)
        parser.add_argument('--repos', type=str,default=None)
        args = parser.parse_args()
        try: 
            ret = excuteCmd(args.local,args.repos,2)
            print(ret) 
        except TimeoutError: 
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
            print("error")
