# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼。
# 最多輸入三次密碼
# 若密碼錯誤，顯示"密碼錯誤，剩下_次機會。"
# 若密碼正確，顯示"登入成功。"

password = 'a123456'
i = 3 #可輸入的次數
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功!')
		break # 結束迴圈
	else:
		i = i - 1
		print('密碼錯誤，還有', i, '次機會。')
		if i == 0:
			break
