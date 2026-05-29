
price = int(input("Nhập số tiền hóa đơn ban đầu: "))

if price > 500000:
    discount_price = price * 0.1
else :
    discount_price = 0

final_price = price - discount_price

print(f"""
--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---
    Số tiền được giảm giá: {discount_price} VND
    Tổng tiền khách phải trả: {final_price} VND
""")