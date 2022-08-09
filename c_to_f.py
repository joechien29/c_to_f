# 攝氏溫度轉換為華氏溫度
# 讓使用者輸入攝氏溫度(C')，將答案轉換為華氏溫度(F')

temp_c = input("請輸入攝氏溫度: ")
temp_c = float(temp_c)
temp_f = temp_c * 9 / 5 + 32
print("轉換後的華氏溫度為: ",temp_f)