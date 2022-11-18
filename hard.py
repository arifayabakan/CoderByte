#StringChallenge


'''
Have the function StringChallenge(str) read str which
will be a string of roman numerals being used are: I for
1, V for 5, X for 10, L for 50, C for 100, D for 500 and
M for 1000. Your program should return the same number given
by str using a smaller set of roman numerals. For example: 
if str is "LLLXXXXVVVV" this is 200, so your program should
return CC because this is the shortest way to write 200 using
the roman numeral system given above. If a string is given
in its shortest form, just return that same string.
'''



#Example_1

print("\nEXAMPLE1\n")

def StringChallenge_1(strParam):  
    s=list(strParam)
    total = 0
    new_roman=''
    d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    d2={1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
  
    for i in range(len(s)): total += (d[s[i]])
  
    bolen=[1000,500,100,50,10,5,1]
    
    kalan = total
    print(s[i], d[s[i]], total)

    '''

    Burada önemli nüans, s[i], indeksin karşılığını verir, indeksi vermez. Karıştırdığım nokta tam olarak burası.
    Elemanın son değerinin indeksi 4, bu indekse karşılık gelen elemandaki değer L, L değerine karşılık gelen
    d[s[i]] değeri de, L key'in karşılığı olan value = 50 olmaktadır. Döngü işlemindeki her bir elemana karşılık gelen
    value toplandığında, total'e eklenir.

    '''

    while kalan != 0:
        for i in range(len(bolen)):
            if bolen[i] <= total:
                bolum = total // bolen[i]
                kalan = total % bolen[i]
                new_roman += d2[bolen[i]]*bolum
                total = kalan
            print(bolum,kalan,new_roman,total)
            
            '''
            Burada da, eğer toplam sayı bölenden büyükse, doğrudan tüm toplamı, bölen listesindeki elemanlara sırayla bölerek, 
            kalanını da bularak hem bölümü hem kalanı elde etmiş. sonrasında, d2 listsinde bölen değerine karşılık gelen harfleri
            bölüm ile çarparak ve birbirine ekleyerek, roma rakamı olarak sonucu elde etmiş. Burada önemli nokta, bolen listesinin
            en büyük sayıdan küçük sayıya doğru sıralanmış olmasıdır.

            '''
        return new_roman

# keep this function call here 
print (StringChallenge_1("DDLL"))


print("\nEXAMPLE2\n")

#Example_2

def StringChallenge_2(strParam):  
    a = {"X" : 10 , "I" : 1 ,"V" : 5 , "L" : 50, "C" : 100, "D" : 500 , "M" : 1000}
    c = {1000 : "M", 500 : "D", 100:"C" , 50 :"L" , 5:"V" , 10:"X" , 1:"I"}
    summ = 0
    for i in range(len(strParam)):
        b= a[strParam[i]]
        summ += b
        print(strParam[i],  b, summ) 
        '''Giriken input: strParam, input uzunluğu len(strParam), 
        input uzunluğu kadar döngüye sokmalıyız ki ilk olarak
        her elemanı a listesinden, i'nin hangi karakterleri temsil
        ettiğini döndürerek (strParam[i]), bu karaktere karşılık gelen değerleri
        b'ye eşitleyerek ve ardından bunların toplamını her bir b'yi toplayarak alabilelim.           
        '''
        

    if(summ in c.keys()):
        return c[summ] #Eğer, toplam doğrudan eşitse c key'lerinden birine, direk o değeri yazdırır, aşağıdaki işlemleri yapmadan.
    else:
        n1 = summ // 1000
        k1 = summ %1000
        n2 = k1 // 500
        k2 = k1 % 500
        n3 = k2 // 100
        k3 = k2 % 100
        n4 = k3 // 50
        k4 = k3 % 50
        n5 = k4 // 10
        k5 = k4 % 10
        n6 = k5 // 5
        k6 = k5 % 5
        n7 = k6 // 1
        print(summ, k1,k2,k3,k4,k5,k6) #AÇIKLAMA 
        print(n1,n2,n3,n4,n5,n6,n7) #AÇIKLAMA
        result = n1*c[1000]+n2*c[500]+n3*c[100]+n4*c[50]+n5*c[10]+n6*c[5]+n7*c[1] 

        '''
        Eğer toplam, karakter uzunluğuna eşit değilse, en büyük sayıdan başlayacak şekilde, bölünen olarak
        ilk olarak toplam olacak şekilde, bölüm ve kalan bulunur. Ardından, her kalan, bir sonraki büyük sayıya bölünerek
        yine bölüm ve kalan bulunur. Bölüm bulma sebebi, c listesindeki sayılar, bu toplamda kaç kere var sonucuna ulaşmaktır. 
        Toplamı en büyük sayıya böldükten sonra her kalanı bir sonraki sayıya bölgeriz ki, kalanda kaç kere bölünen sayı olduğunu
        anlayabilmek için. Ardınadn, sonuçlardan da anlaşılacağı üzere, c listesindeki böldüğümüz sayıya karşılık gelen sayıları 
        bölüm ile çarparak, sayıyı elde ederiz.
        Print olarak da, bu result'a karşılık gelen key'in karşılığı olan value değeri ekrana yazdırılır.
        '''
        return result




# keep this function call here 
print(StringChallenge_2("DDLL"))

print("\nEXAMPLE 3\n")

#Example_3

def StringChallenge_3(strParam):
    mylist = []
    mynumber = 0
    mydict={'M':1000,'D':500,'C':100,'L':50, 'X':10, 'V':5,'I':1 }
  
    for char in strParam: 
        mynumber += mydict[char]  

        '''
        Doğrudan, harfleri temsil eden sayılar toplanmış.
        
        '''
    for rome,number in mydict.items():
        if mynumber >= number:
            while mynumber>=number:
                mylist.append(rome)
                mynumber-=number
    return ("".join(mylist))    
# keep this function call here 
print (StringChallenge_3("DDLL"))

print("\nEXAMPLE 4\n")

#Example_4

def StringChallenge_4(strParam):
    num_dict={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    total=0
    for i in strParam:
        total+=num_dict[i]

    sorted_num_dict=dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
    string_value=str()

    while total>0:
        for key, value in sorted_num_dict.items():
            if total-value>=0:
                total-=value
                string_value+=key
            return string_value
print(StringChallenge_4("DDLL"))