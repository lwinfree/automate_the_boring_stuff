spam=['apple','banana','tofu','cat']
def comma(list):
	count=0
	string=''
	while count < len(list)-1:
	    string += list[count] + ', '
	    count+=1
	return string + 'and ' + list[count]

print (comma(spam))


	    
