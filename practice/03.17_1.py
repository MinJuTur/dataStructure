L1 = [1, 2, 3]
L2 = [1, 2, 3] 
L3 = L1 #L1의 주소값을 L3에 저장

print(L1 == L2) # ==: 내용이 같으냐?
print(L1 is L2) # is: 주소값이 같으냐? 

print(L1 == L3)
print(L1 is L3)