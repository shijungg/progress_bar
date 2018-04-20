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
        info_percent = ('\033[0;34m %d \033[0m' % (self.current_step / float(self.max_step) * 100)) + '\033[0;34m% \033[0m'
        #The progress bar graph
        cnt_current_block = int((self.current_step / float(self.max_step)) * self.bar_length)
        info_current_block = ['\033[0;34m█\033[0m'] * cnt_current_block
        info_rest_block = ['█'] * (self.bar_length-cnt_current_block)
        #The step information
        info_count = '\033[0;33m' + ' ' + str(self.current_step)+'/'+str(self.max_step) + '\033[0m'
        
        sys.stdout.write(
            info_percent+
            ''.join(info_current_block)+
            ''.join(info_rest_block)+
            info_count+
            '\r')
        sys.stdout.flush()

    def end(self):    
        #When you finish your job, call this function to start with a new line
        sys.stdout.write('\n')
        sys.stdout.flush()
