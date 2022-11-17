import time
user_weight = input('Please enter your weight in in either lbs(pounds) or kgs(kilograms): ')
weight = user_weight.lower()
#find if kgs or lbs is specified, then turn input into float for conversion
if weight.find('kgs') != -1:
    weight_int = float(weight.replace('kgs', ''))/.453592
    print(f"Your weight is ({round(weight_int,2)})lbs")
elif weight.find('lbs') != -1:
    weight_int = float(weight.replace('lbs', '')) * .453592
    print(f"Your weight is ({round(weight_int,2)})kgs")
#If units not specified, return print note with both options.
else:
    weight_int = weight.replace('kgs', '') or weight.replace('lbs', '')
    weight_in_lbs = float(weight_int) / .453592
    weight_in_kgs = float(weight_int) * .453592
    print(f"Your weight is either ({round(weight_in_lbs,2)})lbs or ({round(weight_in_kgs,2)})kgs, but you did not include your units so I am not sure.")


print(" Dont worry we wont tell anyone... Good bye")

time.sleep(6)



