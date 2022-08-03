
weight=input('Please enter your weight in in either lbs(pounds) or kgs(killograms): ')
weight_in_kg =  int(weight)*.453592
weight_in_lbs =  int(weight)/.453592
#if weight contains "lbs"
  #take numerical value and multiply it by () after turning it into an int
    #make sure it can take lower or uppercase
#if weight contains "kgs"
  #take numerical value and multiply it by () after turning it into an int
    #make sure it can take lower or uppercase
#if weight !contain "kgs" or "lbs"
print(f"Your weight is either ({weight_in_lbs})lbs or ({weight_in_kg})kgs, but you did not include your units so I am not sure.")


