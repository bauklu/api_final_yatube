# api_final
api final


Логика API находится в приложении api

В проекте используется аутентификация по JWT токену

Аутентифицированный пользователь авторизован на изменение и удаление своего
контента; в остальных случаях доступ предоставляется только для чтения. 
При попытке изменить чужие данные возвращается код ответа 403 Forbidden

Для взаимодействия с ресурсами настроены следующие эндпоинты:
    api/v1/api-token-auth/ (POST)
    api/v1/posts/ (GET, POST)
    api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)
    api/v1/groups/ (GET)
    api/v1/groups/{group_id}/ (GET)
    api/v1/posts/{post_id}/comments/ (GET, POST)
    api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)
