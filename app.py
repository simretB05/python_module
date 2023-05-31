import random
# import antigravity 
import helpers.log
import wikipedia
try:
    user_input=input('which page do you want to see?')

    result=wikipedia.page(user_input)
    print(result.title)
    print(result.content) 
except PageError(title):
  print('please add a correct title')
except:
   print('something went wrong')

my_random_num= random.randint(-100,100)
if(my_random_num>=50):
    print('Winner')
else:
    print('loser')

helpers.log.addLogging('this')
helpers.log.addLogging('is')
helpers.log.addLogging('new')



