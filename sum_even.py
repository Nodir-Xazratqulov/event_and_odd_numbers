#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".


n = 4328
a = n%10
b = n//10
s = b%10
d = n//100
e = d%10
f = d//10
result = a*((a+1)%2)+s*((s+1)%2)+e*((e+1)%2)+f*((f+1)%2)
print(result)