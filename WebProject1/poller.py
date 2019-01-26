import time, app

def main():
    while True:
        val = app.getTable()
        #print(val)
        for i in val:
            app.update(i[1], i[0])          
        time.sleep(30)
        
main()
