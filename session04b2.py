total_price = 0
high_day_price = 0

for day in range(1, 8):
    price = int(input(f"Nhập doanh thu ngày {day}: "))
    total_price += price

    if price > 5000000 :
        high_day_price += 1

avg_price = total_price // 7
    
print(f"""
--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---
    Tổng doanh thu cả tuần: {total_price} VND
    Doanh thu trung bình mỗi ngày: {avg_price} VND
    Số ngày đạt mục tiêu: {high_day_price} ngày
""")