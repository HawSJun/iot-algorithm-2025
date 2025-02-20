# 전역변수
moneyAry = [7, 5, 11, 6, 9, 80000, 10, 6, 15, 12]

# 함수선언
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

# 메인코드
print(f'용돈 정렬 전 -> {moneyAry}')
moneyAry = selectionSort(moneyAry)
print(f'용돈 정렬 후 -> {moneyAry}')
print(f'용돈 중앙값 -> {moneyAry[len(moneyAry)//2]}')