import time
user_weight = input('Please enter your weight in in either lbs(pounds) or kgs(kilograms): ')
weight = user_weight.lower()
if weight.find('kgs') != -1:
    weight_int = weight.replace('kgs', '')
    weight_in_lbs = float(weight_int)/.453592
    print(f"Your weight is ({weight_in_lbs})lbs")
elif weight.find('lbs') != -1:
    weight_int = weight.replace('lbs', '')
    weight_in_kgs = float(weight_int) * .453592
    print(f"Your weight is ({weight_in_kgs})kgs")
else:
    weight_int = weight.replace('kgs', '') or weight.replace('lbs', '')
    weight_in_lbs = float(weight_int) / .453592
    weight_in_kgs = float(weight_int) * .453592
    print(f"Your weight is either ({weight_in_lbs})lbs or ({weight_in_kgs})kgs, but you did not include your units so I am not sure.")


print(" Dont worry we wont tell anyone... Good bye")

time.sleep(4)
