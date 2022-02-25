# caps-api
> `caps-api` - это небольшой пробный проект. Здесь проверялось мое умение в веб-программирование, а именно, в back-end.

[![Build Status](https://img.shields.io/static/v1?label=status&message=deployed&color=blueviolet)](https://caps-api.herokuapp.com/)  
[![License: MIT](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)](https://opensource.org/licenses/MIT) 


API представляет собой набор супер базовых методов для взаимодействия мобильного приложения с базой данных.

## Методы
Из реализованных методов:
- [x] *'/'*: @GET. Выводим имя API.
- [x] *'/api/v1/caps/?number_page=<number_page>, pg_size=<pg_size>'*: @GET. Получение "страницы" данных из базы. *(см. '/redoc')*
- [x] *'/api/v1/caps/{<cap_id>}'*: @GET. Получение конкретной кепки по `id`.
- [x] *'/api/v1/brands/{<brand_id>}/'*: @GET. Получение конкретного бренда по `id`.
- [x] *'/media/{file_path:path}'*: @GET. Получение медиа-файлов.
- [x] *'/vkauth'*: @GET Возможность авторизации в ВК. *(Нельзя пользоваться напрямую, см. Ниже.)*

В планах:
- [ ] *'/api/v1/add-to-favor'*: @POST. Добавляет в базу данных для конкретного пользователя `id` определенного товара.

## Авторизация.
Авторизоваться в приложении можно только при помощи ВК. 
Для этого на стороне клиента необходимо послать соответсвующий запрос используя `app_id` 
приложения, которое зарегестрировано как `caps-api`.

## Deploy
API развернуто на Heroku [здесь](https://caps-api.herokuapp.com/).
