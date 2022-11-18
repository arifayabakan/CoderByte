#MathChallenge
'''
Have the function MathChallenge(num) take the num
parameter being passed and return the string true
if the parameter is a prime number, otherwise return
the string false. The range will be between 1 and 2^16.
'''

#Asal sayılar: Kendisinden ve 1’den başka böleni olmayan sayılardır.

#Example_1


def MathChallenge_1(num):  
    if num == 1:
        return "False"

    '''
    range(5) fonksiyonu, 5'e kadar olan sayıları yani 0,1,2,3,4 değerlerini ifade eder.
    range(2,5) fonksiyonu 2'den başlayıp 5'e kadar olan sayıları 2,3,4 değerlerini ifade eder.
    range(2,5,2) fonksiyonu ise 2'den başlayıp 5'e kadar 2'şer artırarak devam eder, 2,4 değerlerini ifade eder.
    '''
    for i in range(2,num):
        if num%i == 0:
            return "False"
    #Buradaki print fonksiyonları adımları görebilmek amacıyla yazılmıştır.
    print(num)
    print(i) #Son elemanı gösteriyor.
    print(num%i) #Son elemana bölümünden kalanı gösteriyor.
    return "True"

print(MathChallenge_1(11))


#Example_2

def MathChallenge_2(num):
    if num>1:
        return isPrime(num)
    return False
def isPrime(num):
    upper=int(num/2)+1
    for i in range(2,upper):
        if num%i==0:
            return False
    return True   
# keep this function call here 
print(MathChallenge_2(5))

#Example_3

def MathChallenge(num):
  if num == 2:
    return "True"
  if num%2 == 0:
    return "False"
  for i in range(3,int(num**0.5)+1,2):
    if num%i== 0:
      return "False"
  return "True"

# keep this function call here 
print(MathChallenge(13))