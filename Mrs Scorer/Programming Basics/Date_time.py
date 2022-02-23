import datetime as d
now = d.datetime.now()
date_string = '21 June, 2018'
date_obj = d.datetime.strftime(date_string, '%d %B, %Y')
print(date_obj)