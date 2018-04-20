#coding:utf-8
import sys

class ProgressBar():
    current_step = 0
    max_step = 0
    bar_length = 40

    def __init__(self, max_step):
        self.max_step = max_step
        
    def show_progress(self):
        #Every time you call this function, the progress bar will be updated by one step
        self.current_step += 1

        #The percentage information
        info_percent = str(self.current_step / float(self.max_step) * 100) + '% '
        #The progress bar graph
        cnt_current_block = int((self.current_step / float(self.max_step)) * self.bar_length)
        info_current_block = ['█'] * cnt_current_block
        info_rest_block = [' '] * (self.bar_length-cnt_current_block)
        #The step information
        info_count = str(self.current_step)+'/'+str(self.max_step)
        
        sys.stdout.write(
            info_percent+
            '|'+
            ''.join(info_current_block)+
            ''.join(info_rest_block)+
            '|'+
            info_count+
            '\r')
        sys.stdout.flush()

    def end(self):    
        #When you finish your job, call this function to start with a new line
        sys.stdout.write('\n')
        sys.stdout.flush()
