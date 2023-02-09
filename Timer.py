import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        '''
        The line in the code, {:02d}:{:02d}’.format(mins, secs) Indicates that 
        there should be two in mins and two digits in seconds as the mins 
        and secs are represented in the format() function.
        '''
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
t = input("Enter the time in seconds: ")
countdown(int(t))
print('Time`s Up!')