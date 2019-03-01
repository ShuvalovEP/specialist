import datetime 

def creator(komu):
    def add_mess(report):
        def batt_rep(msg):
            dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return dt + msg + komu
        return batt_rep
    return add_mess

@creator('Evgenys')
def func(mess):
    return

func(' пока ')
