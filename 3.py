#Answer 3
desired_output=[]
import re
list=(re.split("[,;_]","A, very very; irregular_sentence"))
print(list)
for i in list:
    print(i+" ",end="")
