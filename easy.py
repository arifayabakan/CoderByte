#ArrayChallenge
'''
Have the function ArrayChallenge(strArr) take the array 
of strings stored in strArr, which will only contain two
strings of equal length that represent binary numbers, 
and return a final binary string that performed the bitwise
AND operation on both strings. A bitwise AND operation places
a 1 in the new string where there is a 1 in both locations
in the binary strings, otherwise it places a 0 in that spot.
For example: if strArr is ["10111","01101"] then your program 
should return the string "00101"
'''

#Example_1

def ArrayChallenge_1(strArr):
    
    result=""
    for i in range(0, len(strArr[0])):
        if strArr[0][i] == "1" and strArr[1][i] == "1":
            result+="1"
        else:
            result+="0"
    
    print("Example_1 ALGORİTMA AÇIKLAMASI:\n" #ALGORİTMA AÇIKLAMASI BU METİNDEDİR!
    
    "\nBurada, {0} ilk eleman, ikinci eleman ise {1} elemanıdır. \n"
    "\ni harfi ile ise elemanın karakterleri temsil edilmektedir."  
    "\nHer iki sayının elemanlarının 1'e eşit olup olmadığı kontrol edilir."
    "\nHer iki eleman da 1'e eşitse, sonucun içine o elemanlar adına 1 yazar." 
    "\nDeğilse, o elemanlar adına 0 yazar."
    .format(strArr[0],strArr[1]))

    return result
print("Example_1 sonucu:", ArrayChallenge_1(["100","000"]), "\n")

#Example_2

def ArrayChallenge_2(strArr):  
    first = strArr[0]
    last = strArr[1]
    output = ""
    for i in range(0,len(first)):
        if int(first[i]) == 1 and int(last[i]) == 1:
            output += "1"
        else:
            output += "0"

        print("Example_2 ALGORİTMA AÇIKLAMASI:\n"  #ALGORİTMA AÇIKLAMASI BU METİNDEDİR!
    "\nBurada, first olarak tanımlanan {0} ilk eleman, ikinci eleman ise" 
    "\nlast olarak tanımlanan {1} elemanıdır. i harfi ile ise elemanın karakterleri temsil edilmektedir."  
    "\nHer iki sayının elemanlarının 1'e eşit olup olmadığı kontrol edilir."
    "\nHerhangi bir elemanın uzunluğunda bir for döngüsü kurulmuş." 
    "\nBurada first tercih edilmiş, ancak, eleman uzunluğu aynı olduğu için," 
    "\nlast da tercih edilebilir."
    "\nHer iki eleman da 1'e eşitse, output içine o elemanlar adına 1 yazar." 
    "\nDeğilse, o elemanlar adına 0 yazar.")
  # code goes here
    return output

# keep this function call here 
print("Example_2 sonucu:" , ArrayChallenge_2(["100","000"]), "\n")

#Example_3

def ArrayChallenge_3(strArr):  
    a=strArr[0]
    b=strArr[1]
    newstr=[]

    for i in range(0,len(a)):
        if (a[i]=="1") and (b[i]=="1"):
            newstr.append(1)
        else:
            newstr.append(0)

    s=[str(i) for i in newstr]

    print("Example_3 ALGORİTMA AÇIKLAMASI:\n" #ALGORİTMA AÇIKLAMASI BU METİNDEDİR!
    
    "\nBurada, diğer iki örnekten FARKLI olarak string olarak değil," 
    "\nlistede integer eleman olarak döngü oluşturulmuştur." 
    "\n{0} ilk eleman, ikinci eleman ise {1} elemanıdır."
    "\ni harfi ile ise her iki listedeki aynı olan eleman sayısıdır."  
    "\nHer iki listede bulunan sayının elemanlarının 1'e eşit olup olmadığı kontrol edilir."
    "\nHer iki listede bulunan sayının eleman da 1'e eşitse, newstr içine o elemanlar adına 1 yazar." 
    "\nDeğilse, o elemanlar adına 0 yazar."
    .format(a,b))

    return("".join(s))

# keep this function call here 
print("Example_3 sonucu:" , ArrayChallenge_3(["11100","10100"]), "\n")




