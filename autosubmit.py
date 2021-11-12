import os
import time
import subprocess
import argparse
 
class TimeoutError(Exception):
    pass 
 
def excuteCmd2(local,repos, timeout = 1):

        
        res = os.popen('git init')
        output_str = res.read()   # 获得输出字符串
        print(output_str)
        time.sleep(2)
        res = os.popen('git add .')
        output_str = res.read()   # 获得输出字符串
        print(output_str)
        time.sleep(2)
        res = os.popen('git remote add  origin '+repos)
        output_str = res.read()   # 获得输出字符串
        print(output_str)
        time.sleep(2)
        res = os.popen('git push origin master')
        output_str = res.read()   # 获得输出字符串
        print(output_str)
        time.sleep(2)
        res = os.popen('yes')
        output_str = res.read()   # 获得输出字符串
        print(output_str)
        time.sleep(2)
        res = os.popen('exit')
        output_str = res.read()   # 获得输出字符串
        print(output_str)
        time.sleep(2)
        return
def excuteCmd(local,repos, timeout = 1):
        s = subprocess.Popen("C:\Windows\System32\cmd.exe",stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell = True)
        #out, err =s.communicate('cd '+local+'\n')
        #print(out)
        time.sleep(2)
        s.stdin.write(str.encode('git init \n'))
        #print(s.stdout.write())
        time.sleep(2)
        s.stdin.write(str.encode('git add . \n'))
        #print(s.stdout.write())
        time.sleep(2)
        s.stdin.write(str.encode('git remote add  origin git@github.com:Ren-Xuan/LeetCode.git \n'))
        #print(s.stdout.write())
        time.sleep(2)
        s.stdin.write(str.encode('git commit -m '+str(time.time()) +"\n"))
        time.sleep(2)
        s.stdin.write(str.encode('git push origin master\n'))
        #print(s.stdout.write())
        time.sleep(2)
        out, err =s.communicate(str.encode('yes\n'))
        print(out.decode(encoding='gbk'))
        time.sleep(2)
        #s.stdin.write(str.encode('exit\n'))
        #print(s.stdout.write())
        #time.sleep(2)
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
            print("error")
