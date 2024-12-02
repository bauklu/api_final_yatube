# api_final
api final


Логика API находится в приложении api

В проекте используется аутентификация по JWT токену

Аутентифицированный пользователь авторизован на изменение и удаление своего
контента; в остальных случаях доступ предоставляется только для чтения. 

При попытке изменить чужие данные возвращается код ответа 403 Forbidden
При попытке запроса несуществующего объекта код ответа 404 Not_Found
При попытке запроса неавторизованного пользователя к эндпойнту 
    api/v1/follow/ код ответа 401 Unauthorized

Для взаимодействия с ресурсами настроены следующие эндпоинты:

    Получить (обновить, проверить) токен
        api/v1/jwt/create/ (POST)  
        api/v1/jwt/refresh/ (POST)
        api/v1/jwt/verify/ (POST)
    
    Получить, создать, обновить, удалить
        
        пост:
        api/v1/posts/ (GET, POST)
        api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)

        комментарий:
        api/v1/posts/{post_id}/comments/ (GET, POST)
        api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)

        сообщество:
        api/v1/groups/ (GET)
        api/v1/groups/{group_id}/ (GET)

        подписка:
        api/v1/follow/ (GET, POST)
