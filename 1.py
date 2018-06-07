#Answer 1
desired_output=[]
import re
tup_1=(tuple)(re.split("\W","zuck26@facebook.com"))
tup_2=(tuple)(re.split("\W","page33@gmail.com"))
tup_3=(tuple)(re.split("\W","jeff42@amazon.com"))
desired_output.append(tup_1)
desired_output.append(tup_2)
desired_output.append(tup_3)
print("Printing the desired output:")
print(desired_output)
