# Приветствие программы
# counter - баллы за ответ (10 за один правильный, 0 - за неправильный)
# score - количество правильных ответов на вопрос
# progress_procent - расчет процента правильных ответов

counter = 0
score = 0

user_name = input("Привет! Предлагаю проверить свои знания английского! Расскажи, как тебя зовут!\n")
print(f"Привет {user_name}, начинаем тренировку!")

# Вопрос №1

answer_1 = str(input("My name ___ Vova\n"))
is_answer_1_true = answer_1 == "is"

if is_answer_1_true:
        counter += 10
        score += 1
        print(f"Ответ верный!\n Вы получаете {counter} баллов")
if not is_answer_1_true:
        counter = counter
        score = score
        print(f"Неверно!\n Правильный ответ {is_answer_1_true}\n")

# Вопрос №2

answer_2 = str(input("I ___ coder\n"))
is_answer_2_true = answer_2 == "am"

if is_answer_2_true:
        counter += 10
        score += 1
        print(f"Ответ верный!\n Вы получаете {counter} баллов")
if not is_answer_2_true:
        counter = counter
        score = score
        print(f"Неверно!\n Правильный ответ {is_answer_2_true}\n")

# Вопрос №3

answer_3 = str(input("I live ___ Moscow\n"))
is_answer_3_true = answer_3 == "in"

if is_answer_3_true:
        counter += 10
        score += 1
        print(f"Ответ верный!\n Вы получаете {counter} баллов")
if not is_answer_3_true:
        counter = counter
        score = score
        print(f"Неверно!\n Правильный ответ {is_answer_3_true}\n")


# Прощание программы

progress_procent = round(score * 100/3)

print(f"Вот и все, {user_name}!")
print(f"Вы ответили на {score} вопросов из 3 верно.")
print(f"Вы заработали {counter} баллов.")
print(f"Это {progress_procent} процентов.")
