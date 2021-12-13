import time
import subprocess
import argparse
import schedule
class TimeoutError(Exception):
    pass 

def excuteCmd(repos, timeout = 2):
        cur = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(cur)
        with open('./test.txt', 'w') as f:
            f.write(cur)
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
        parser.add_argument('--repos', type=str,default=None)
        args = parser.parse_args()
        print(args.repos)
        cur = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(cur)
        try: 
            
            schedule.every().day.at('02:30').do(excuteCmd,args.repos)
            schedule.every().day.at('10:24').do(excuteCmd,args.repos)
            schedule.every().day.at('18:24').do(excuteCmd,args.repos)
            schedule.every().day.at('22:24').do(excuteCmd,args.repos)
            #schedule.every(1).minutes.do(excuteCmd,args.repos)
            while True:
                schedule.run_pending()
                time.sleep(57)
            #ret = excuteCmd(args.local,args.repos,2)
            #print(ret) 
        except TimeoutError: 
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
            print("error")