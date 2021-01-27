def write_1(a): #10-15e kadar olan sayilari yazdimak icin olusturulan fonksiyon ve dictionary
    dict_other={'10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen'}
    print(dict_other[a])   

def write_2(a): # iki basamakli dictonary disindaki sayilari yazdirmak icin olusturulan fonksiyon
    number_list1=['1','2','3','4','5','6','7','8','9'] #rakamlari kontrol icin olusturulan liste
    woord_list1=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']#kontrol sonrasi tespit edilen rakamlrin yazili oldugu liste
    woord_list10=['Teen','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']#kontrol sonrasi tespit edilen rakamlrin yazili oldugu liste 10 ar
    result="" #tespti edilen yazi degerinin eklendigi degisken
    control_0=a[0] #girilen sayinin 0 indisindeki ifade(str)
    control_1=a[1] #girilen sayinin 1 indisindeki ifade(str)    
                  
    if control_1=='0': #sayinin 1. indexindeki rakam 0 ise 20 30 vd.(ten haric o ust fonksiyonda)
        found_ind=number_list1.index(control_0) #rakamin number_list deki indeksi tespit edilir,
        result+=woord_list10[found_ind]     #karsiligi olan woor_list deki yazi result a eklenir, 
    elif control_0==control_1:            #rakamlar ayni ise 22, 33 gibi;
        found_ind=number_list1.index(control_0)#indeks bulunur
        result+=woord_list10[found_ind]#indeksin karsiligi woord listede bulunur resulta eklenir
        result+=' '                     #yazilari ayirmak icin bosluk eklenir,
        result+=woord_list1[found_ind]  #rakamlar ayni oldugu icin ikinci rakam woord list1 den eklenir   
    elif control_0=='1':                #ilk rakam bir oldugunda(dictionary de olmayan sayilar 16-19)
        found_ind=number_list1.index(control_1)#indeks tespit edilir,
        result+=woord_list1[found_ind]  #woordlist1 den result a eklenir
        #result+=' '                    #bitisik yazildigi icin bosluk birakilmaz
        found_ind=number_list1.index(control_0) #indeks tespit edilir
        result+=woord_list10[found_ind]          #woord_list10 dan result a eklenir  
    elif control_0!=control_1:          #rakamlar farkli oldugu durumlardaa 
        found_ind=number_list1.index(control_0) #ilk rakakmin indeksi tespit edilir,
        result+=woord_list10[found_ind] #woord_list10 dan result a eklenir,
        result+=' '                     #bosluk eklenir,
        found_ind=number_list1.index(control_1)     #ikinci rakam indeks tespti edilir,   
        result+=woord_list1[found_ind]              #woord_list1 den rusult a eklenir,
    
    print(result)

number_user=(input('Lutfen iki basamakli bir sayi girin: ')) #kullanicidan giris alinir,
if int(number_user)<16: #int. e cevrilir ve eger 16 dan kucuk ise write1(ilk fonksiyon cagrilir)
    write_1(number_user) #ilk fonksiyonun cagrilir,
else:
    write_2(number_user) #degilse write2(ikinci fonksiyon ) cagrilir,
