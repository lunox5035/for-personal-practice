# print ("Hello Woerd!")

#  2부터30까지 소수리스트 뽑아내기
listi=list(range(2,31))     #2~30리스트
for i in range(2,31):       
    for e in range(2,i):    #나누는 수, 1과 i가 아닌 수 
        if i==e:            
            continue        
        elif i%e==0:        #소수가 아닌 수 제거
            listi.remove(i)
            break
print(set(listi))           #출력