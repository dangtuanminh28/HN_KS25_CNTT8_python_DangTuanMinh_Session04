number = 79

for count in range(1, 6):
    guess_num = int(input(f"Lượt đoán {count} - Nhập số của bạn: "))

    if guess_num < number :
        print("Gợi ý: Số của bạn NHỎ hơn mã số may mắn!")
    elif guess_num == number:
        print("Chúc mừng! Bạn đã đoán chính xác số may mắn!")
        break
    else :
        print("Gợi ý: Số của bạn LỚN hơn mã số may mắn!")

    if count == 5:
        print("Chúc bạn may mắn lần sau!")
        break

print("--- TRÒ CHƠI KẾT THÚC ---")