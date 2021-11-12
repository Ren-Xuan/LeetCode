import schedule
def job(val):
  print(f'hello {val}')
# schedule.every(2).seconds.do(job)
# 使用带参数的do方法
schedule.every(2).seconds.do(job, "linux")
 