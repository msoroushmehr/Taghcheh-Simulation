from . import jalali
from django.utils import timezone
def numbers_convertor(mystr):
    numbers = {
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
        "0":"۰"
    }
    for e, p in numbers.items():
        mystr = mystr.replace(e,p)
    return mystr    
    
def jalali_convertor(time):
    time = timezone.localtime(time)
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    jalali_month = [
        "فروردین",   "اردیبهشت",    "خرداد",    "تیر",    "مرداد",	"شهریور",     "مهر",     "آبان",    "آذر",	"دی",	"بهمن","اسفند"
    ]
    time_to_list = list(time_to_tuple)
    for index, month in enumerate(jalali_month):
        if time_to_list[1] == index + 1:
             time_to_list[1] = month
             break
     
    output = "{} {} {}, ساعت {}:{}".format(
        time_to_list[2], 
        time_to_list[1], 
        time_to_list[0], 
        time.hour, 
        time.minute
        )     
    
    return numbers_convertor(output)
   
             
          
