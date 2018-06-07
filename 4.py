
import re
tweet= "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
print("Tweet:\n",tweet)
str1=re.sub('http[\S]*','',tweet)
str1=re.sub('#[\w]*','',str1)
str1=re.sub('@[\w]*','',str1)
str1=re.sub('[,.;:\'!?]','',str1)
str1=re.sub('RT','',str1)
str1=re.sub('cc','',str1)    
print("Output:\n",str1)
