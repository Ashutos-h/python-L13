#Answer 2
text="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
import re
matcher=re.finditer('[bB]',text)
count=0
for m in matcher:
	count=count+1
	print('Match is at: {}, End: {}, Pattern found: {}'.format(m.start(), m.end(), m.group()))
print('Total count: ',count)