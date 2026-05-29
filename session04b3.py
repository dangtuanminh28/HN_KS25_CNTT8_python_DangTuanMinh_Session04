total_count = int(input("Nhập số lượng hóa đơn trong ca: "))

count = 1
max_price = 0
min_price = 0

while count <= total_count:
    price = int(input(f"Nhập giá trị hóa đơn thứ {count}: "))
    
    if count == 1:
        max_price = price
        min_price = price
    else:
        if price > max_price:
            max_price = price
        if price < min_price:
            min_price = price
            
    count += 1

print(f"""
--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---
Hóa đơn có giá trị cao nhất:  {max_price} VND
Hóa đơn có giá trị thấp nhất: {min_price} VND
""")