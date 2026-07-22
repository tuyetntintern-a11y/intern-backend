"""
Bài 16.
Ask the user to enter a new password. Ask them to enter it again. If the two
passwords match, display “Thank you”. If the letters are correct but in the wrong
case, display the message “They must be in the same case”, otherwise display the
message “Incorrect”
"""
# def check_password(password1, password2):
#     if password1 == password2:
#         return "Thank you"
#     elif password1.lower() == password2.lower():
#         return "They must be in the same case"
#     else:
#         return "Incorrect"
# password1 = input("Enter a new password: ")
# password2 = input("Enter the password again: ")
# print(check_password(password1, password2))

"""
Bài 17.
Viết một chương trình nhập số nguyên dương n và tính tổng của các chữ số của
số n.
Ví dụ:
Nếu người dùng nhập 3141 thì chương trình của bạn nên hiển thị 3 + 1 + 4 + 1 = 9
"""

# def sum_of_digits(n):
#     total = 0
#     for digit in str(n):
#         total += int(digit)
#     return total

# n = input()
# print(sum_of_digits(n))

"""
Bài 18.
Ứng dụng chuyển đổi nhiệt độ từ độ C sang F, chuyển đổi từ kg sang pao(lb),
diện tích, thể tích, tốc độ, thời gian (Easy)
Ý tưởng:
Xây dựng một chương trình gồm nhiều chức năng trên, người dùng chọn:
chức năng 1: Chuyển đổi độ C sang độ F
chức năng 2: Chuyển đổi độ F sang độ C
chức năng 3: Chuyển đổi từ kg sang pao(lb)
chức năng 4: Chuyển đổi từ pao(lb) sang kg
chức năng 5: Chuyển đổi từ mét sang feet
chức năng 6: Chuyển đổi từ feet sang mét
chức năng 7: Thoát chương trình
"""
# def c_to_f(celsius):
#     return (celsius * 9/5) + 32

# def f_to_c(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# def kg_to_lb(kg):
#     return kg * 2.20462

# def lb_to_kg(lb):
#     return lb / 2.20462

# def m_to_ft(meters):
#     return meters * 3.28084

# def ft_to_m(feet):
#     return feet / 3.28084
# while True: #Lặp vô hạn (lặp mãi mãi) cho đến khi gặp break hoặc return.
#     print("Chọn chức năng:")
#     print("1: Chuyển đổi độ C sang độ F")
#     print("2: Chuyển đổi độ F sang độ C")
#     print("3: Chuyển đổi từ kg sang pao(lb)")
#     print("4: Chuyển đổi từ pao(lb) sang kg")
#     print("5: Chuyển đổi từ mét sang feet")
#     print("6: Chuyển đổi từ feet sang mét")
#     print("7: Thoát chương trình")

#     choice = input("Nhập lựa chọn của bạn (1-7): ")

#     if choice == '1':
#         celsius = float(input("Nhập nhiệt độ (°C): "))
#         print(f"{celsius}°C = {c_to_f(celsius)}°F")
#     elif choice == '2':
#         fahrenheit = float(input("Nhập nhiệt độ (°F): "))
#         print(f"{fahrenheit}°F = {f_to_c(fahrenheit)}°C")
#     elif choice == '3':
#         kg = float(input("Nhập khối lượng (kg): "))
#         print(f"{kg} kg = {kg_to_lb(kg)} lb")
#     elif choice == '4':
#         lb = float(input("Nhập khối lượng (lb): "))
#         print(f"{lb} lb = {lb_to_kg(lb)} kg")
#     elif choice == '5':
#         meters = float(input("Nhập chiều dài (m): "))
#         print(f"{meters} m = {m_to_ft(meters)} ft")
#     elif choice == '6':
#         feet = float(input("Nhập chiều dài (ft): "))
#         print(f"{feet} ft = {ft_to_m(feet)} m")
#     elif choice == '7':
#         print("Thoát chương trình.")
#         break
#     else:
#         print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


"""
Bài 19.
Làm trò chơi búa, đá, giấy chơi với máy tính
Ý tưởng:
Gợi ý:
Cách 1: Nhập số từ bàn phím
import random
choice = int(input("User turn: "))
random_choice = random.randint(1, 3)
Cách 2: Nhập chữ từ bàn phím
import random
options = ["Rock","Paper","Scissors"]
AI = random.choice(options)
Người chơi có 5 lượt chơi với máy tính, sau 5 lượt chơi thì thống kê người chơi
đã thắng, hòa, thua bao nhiêu lượt với máy tính.
"""
# def play_rock_paper_scissors():
#     import random

#     options = ["Rock", "Paper", "Scissors"]
#     user_wins = 0
#     computer_wins = 0
#     ties = 0

#     for i in range(5):
#         user_choice = input("User turn (Rock, Paper, Scissors): ").capitalize()
#         computer_choice = random.choice(options)
#         print(f"Computer chose: {computer_choice}")

#         if user_choice == computer_choice:
#             print("It's a tie!")
#             ties += 1
#         elif (user_choice == "Rock" and computer_choice == "Scissors") or \
#              (user_choice == "Paper" and computer_choice == "Rock") or \
#              (user_choice == "Scissors" and computer_choice == "Paper"):
#             print("You win!")
#             user_wins += 1 
#         else:
#             print("Computer wins!")
#             computer_wins += 1  
            
#     print(f"\nFinal Results:")
#     print(f"You won: {user_wins}")
#     print(f"Computer won: {computer_wins}")
#     print(f"Ties: {ties}")
# play_rock_paper_scissors()



"""
Bài 20.

Làm trò chơi đoán câu đố động vật (tên thủ đô các nước)

Ý tưởng:

Chương trình hiển thị danh sách câu hỏi có sẵn, người dùng nhập câu trả lời.

Chương trình kiểm tra câu trả lời là đúng hay sai và đưa ra thông báo.

Người chơi có thể đoán sai tối đa 3 lần, nếu quá thì kết thúc trò chơi.
"""

def city_quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is the capital of Japan?": "Tokyo",
        "What is the capital of Australia?": "Canberra",
        "What is the capital of Canada?": "Ottawa",
        "What is the capital of Brazil?": "Brasília"
    }
    score = 0
    attempts = 0
    max_attempts = 3

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {answer}.")
            attempts += 1
            if attempts >= max_attempts:
                print("You've exceeded the maximum number of incorrect attempts. Game over.")
                break

    return(f"Your final score is: {score}/{len(questions)}")

print(city_quiz())
