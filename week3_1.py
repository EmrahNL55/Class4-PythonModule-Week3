from functools import reduce #reduce fonkisyonu import edilir.
def perfect_number(a):       #perfect number isimli fonksiyon olusturulur.
    while a>1:               #girilen a degeri 1 den buyukse dongu baslatilir,
        list=[]              #pozitif bolen  sayilarin eklenmesi icin bos liste olusturulur,
        
        for x in range(1,a+1): # 1, den 1000 e kadar sayilar range ile x degiskenine aktarilir,
            if a%x==0:          #a  nin x e bolumunden kalan sifir ise sayilar listeye ekleneir,
                list.append(x)  #listeye ekleme islemi
        y=reduce(lambda a,b: a+b, list ) #reduce ve lambda ile listedeki sayilar toplanir,
            
        if y-a==a:                      #almdan a sayisi cikarilir(perfect sayilar kendisi haric diger Poz. bol.top. oldugu icin)
            print(f'{a} !!>>this is a perfect number.') #ekrana yazdima islemi yapilir,
            a-=1                                # a sayisi bir eksiltilir,
            list.clear()                        #bir sonraki hesaplama icin liste bosaltilri,
        else:
            list.clear()                        #condition uymayan durumlarda liste bosaltma ve 1 eksiltme islemi yapilir,
            a-=1
                  
 
perfect_number(1000)
