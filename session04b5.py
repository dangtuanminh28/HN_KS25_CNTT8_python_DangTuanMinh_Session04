is_Done = True

total_bill = 0
total_bills_count = 0
large_bill_count = 0

while is_Done:
    confirm = input("Có muốn tiếp tục nhập hóa đơn không? (C/K): ").strip().upper()
    
    if confirm == "C":
        bill = int(input(f"Khách hàng {total_bills_count + 1} - Nhập giá trị hóa đơn: "))
        total_bill += bill
        total_bills_count += 1
        
        if bill >= 1000000:
            large_bill_count += 1
            
    elif confirm == "K":
        is_Done = False

if total_bills_count > 0:
    percent = (large_bill_count / total_bills_count) * 100
else:
    percent = 0

print(f"""
--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---
Tổng số hóa đơn đã xử lý: {total_bills_count} hóa đơn
Tổng số doanh thu ngày hôm nay: {total_bill} VND
Số hóa đơn lớn từ 1000000 trở lên: {large_bill_count} hóa đơn
Tỷ lệ hóa đơn lớn đạt: {percent}% trên tổng số đơn hàng
""")