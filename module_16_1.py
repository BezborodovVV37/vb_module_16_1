from fastapi import FastAPI

app = FastAPI()

#Для запуска сервера, в терминале используйте команду :  uvicorn module_16_1:app --reload


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def admin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def id_user(user_id: str) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def info(username: str = 'Ric', age: int = 32) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
