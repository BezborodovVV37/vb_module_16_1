from fastapi import FastAPI

app = FastAPI()

# Для запуска сервера, в терминале используйте команду: uvicorn module_16_1:app --reload

@app.get('/')
async def welcome() -> str:
    return "Главная страница"

@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def id_user(user_id: str) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def info(username: str = 'Ric', age: int = 32) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}.'
