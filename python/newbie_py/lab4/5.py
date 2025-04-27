def count_purchased(n):
    m = {}
    for i in range(n):
        a = input("Введите запись о покупке (ID Покупателя Товар Количество): ").split()
        buyer_id = int(a[0])
        item = a[1]
        quantity = int(a[2])
        if buyer_id in m:
            m[buyer_id].append((item, quantity))
        else:
            m[buyer_id] = [(item, quantity)]
    return m

n = int(input("Введите количество записей о покупках: "))
result = count_purchased(n)
for buyer_id, m in result.items():
    print("Покупатель ID", buyer_id)
    for item, quantity in m:
        print(f"Товар: {item}, Количество: {quantity}")
    print()
