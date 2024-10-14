users = [
    {'name': 'Sergio', 'login': 'Sergio123', 'parol': 'I don not need parol!!!!'},
    {'name': 'Nicita', 'login': 'Nicita123', 'parol': 'I don not need parol!!!!'},
    {'name': 'Artur', 'login': 'Artur123', 'parol': 'I don not need parol!!!!'},
    {'name': 'Anastasia', 'login': 'Anastasia', 'parol': 'I don not need parol!!!!'},
    {'name': 'Kat', 'login': 'Kat123', 'parol': 'I don not need parol!!!!'}
]
def check_len(user):  # Проверка длины пароля
    return len(user['parol']) >= 5

def checking_login(user):
    login = user['login']
    # Логин должен содержать только алфавитно-цифровые символы и символ '_'
    return all(char.isalnum() or char == '_' for char in login)

def bed_login(user):
    return not (check_len(user) and checking_login(user))

# Фильтруем пользователей с некорректными логинами или паролями
bed_logins = filter(bed_login, users)

# Выводим сообщения для пользователей с некорректными логинами
for user in bed_logins:
    print(f"Уважаемый {user['name']}, Ваш логин '{user['login']}' не является корректным!")
