#coding:utf-8
import time
from progress_bar_color import ProgressBar

pb = ProgressBar(1000)

for i in range(1000):
    time.sleep(0.1)
    pb.show_progress()
pb.end()
