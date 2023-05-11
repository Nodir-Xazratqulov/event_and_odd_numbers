#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".


n = 2643
a = n%10
b = n//10
s = b%10
d = n//100
e = d%10
f = d//10
result = a%2+s%2+e%2+f%2
print(result)

