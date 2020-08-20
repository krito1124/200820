d = {}
print('welcome to the 高手系統')

while True:
    print('1.建立字典')
    print('2.enter all the 單字')
    print('3.english翻chinese')
    print('4.chinese翻english')
    print('5.test')
    print('6.leave')
    
    option = input('please enter 選項:')
    
    if option == '6':
        break
    elif option == '1':
        while True:
            voc = input('please enter new english word (press 0 to leave:')
            if voc =='0':
                break
            if voc not in d:
                voc_ch = input('enter Chinese:')
                d [voc] = voc_ch
            else:
                print('it is there already')
    elif option == '2':
            s = sorted(d)
            print(s)
            for i in s:
                print(i,':',d[i])
    elif option == '3':
        while True:
            voc = input('please enter the english word(press 0 to leave:')
            if voc == '0':
                break
            if voc in d:
                print(voc,'Chinese is',d[voc])
            else:
                print('there are not this word')
    elif option == '4':
        while True:
            got = False
            ch = input('please enter Chinese word(press 0 to leave:')
            if ch == '0':
                break
            for k,v in d.items():
                if ch == v:
                    print(ch,'的英文是',k)
                    got = True
            if got == False:
                print('there is no this word')
    elif option == '5':
            score = 0
            for k , v in d.items():
                print(v,':')
                answer = input()
                if answer == k:
                    score=score+1
                else:
                    print('wrong')
            print('total',score,'分')