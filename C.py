

t = int(input())  

for _ in range(t):
    n, a, q = map(int, input().split())  
    notifications = input()  

    online_subscribers = a

    for notification in notifications:
        if notification == '+':
            online_subscribers += 1
        else:
            online_subscribers = max(0, online_subscribers - 1)

    if online_subscribers == n :
        print("YES")
    else:
        if online_subscribers >= a or online_subscribers > 0:
            print("MAYBE")
        else:
            print("NO")

