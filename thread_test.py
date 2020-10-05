import threading
import time

def search_time(time_tables):
    while True:
        com_time = time.strftime("%H:%M", time.localtime(time.time()))
        print(com_time +" & "+ time_tables[0])
        print(time_tables.__contains__(com_time))
        time.sleep(2)
        if time_tables.__contains__(com_time) :
            break
        return com_time

# if __name__ == '__main__':
#     time_table = ["22:00","11:00","19:45"]
#     search_time(time_table)
    # time_thread = threading.Thread(target= search_time, args=(time_table))
    # time_thread.start()

# import threading, requests, time
#
# def getHtml(url):
#     resp = requests.get(url)
#     time.sleep(1)
#     print(url, len(resp.text), ' chars')
#
# if __name__ =='__main__':
#     t1 = threading.Thread(target=getHtml, args=('http://google.com',))
#     t1.start()
#     print("### End ###")