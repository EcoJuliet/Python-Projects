# smart count

print ('Smart count')
print ('Primeiro numero: ')
N1 = int(input())
print ('Segundo numero: ')
N2 = int(input())

if N2 > N1:
    count = N1
    while (count <= N2):
        print (str(count)+"...")
        count = count + 1
else:
    count = N1
    while (count >= N2):
        print (str(count)+"...")
        count = count - 1
print ('End of code')
