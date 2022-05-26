from  window_searcher import window_searcher
import time
n = window_searcher()

key = '开源'
res = n.do_search(key)
print(res)
print(len(res))

start_time=time.time()
time.sleep(2)
end_time=time.time()
print('%0.2f'%(end_time-start_time))

import uuid

name = "test_name"
namespace = "test_namespace"

print()  # 带参的方法参见Python Doc

l_uuid=str(uuid.uuid1()).split('-')

s_uuid=''.join(l_uuid)

print(s_uuid.upper())

1D745DC3DD0511EC965884144DB47B38