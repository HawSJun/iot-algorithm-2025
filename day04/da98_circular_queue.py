# da01_circular_queue_exercise.py
# 원형 큐 구현

def isQueueFull():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is Full!')
        return
    else:
        rear = (rear + 1) % SIZE
        queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empyt!')
        return None
    else:
        front = (front + 1) % SIZE
        data = queue[front]
        queue[front] = None
        return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty!')
        return None
    else:
        return queue[(front + 1) % SIZE]

SIZE = int(input('큐 크기를 입력하세요 --> '))
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ =='__main__':
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q) --> ').upper()

        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
            print('front : ', front, 'rear : ', rear)
        elif select == 'E':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
            print('front : ', front, 'rear : ', rear)
        elif select == 'V':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')
            print('front : ', front, 'rear : ', rear)
        else:
            print('입력 오류')

    print('프로그램 종료!')