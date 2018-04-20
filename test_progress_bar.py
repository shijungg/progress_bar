#coding:utf-8
import time
from process_bar import ProcessBar

pb = ProcessBar(1000)

for i in range(1000):
    time.sleep(0.1)
    pb.show_process()
pb.end()
