# 최솟값 구하기
arr = [5, 3, 7, 9, 2, 5, 2, 6]
#float('inf') 파이썬에서의 가장 큰값 
#arrMin=float('inf')
arrMin = arr[0]
for i in range(1,len(arr)):
    if arrMin > arr[i] :
        arrMin = arr[i]

print(arrMin)
