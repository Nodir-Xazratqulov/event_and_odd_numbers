#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_odd" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".

n = 4328
a = n%10
b = n//10
s = b%10
d = n//100
e = d%10
f = d//10
result = a*(a%2)+s*(s%2)+e*(e%2)+f*(f%2)
print(result)

