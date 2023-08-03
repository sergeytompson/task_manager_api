# Company Test Task

## Описание
Это тестовое задание в виде вэб-приложения, которое предоставляет api для представления структуры
компании: ее департаментов и работников. С текстом тестового задания можно ознакомиться [тут](ТЗ.txt).
Приложение имеет следующие сущности:
### Департамент (Department)
Имеет имя и может иметь директора (одного из сотрудников по связи один-к-одному).
### Сотрудник (Worker)
Имеет ФИО, фото, оклад, возраст и может относится к одному из департаментов в компании (связь один ко многим). 

## Стек
+ Python 3.10
+ Django 4.2
+ Django Rest Framework 3.14

## API
- '/swagger/' - страница с документацией проекта.
- '/api/department/' - страница со списком всех департаментов. Объекты департаменов содержат дополнительные строки:
workers_count (количество сотрудников департамента), department_salary (общая зарплата сотрудников департамента).
- '/api/performer/<id департамента>' - страница с информацией о конкретном департаменте.
- '/api/worker/' - страница сo списком всех работников. Струница имеет пагинацию (по 5 работников на страницу). GET-запрос
может принимать дополнительные параметры: department_id (фильтрует работников по принадлежности к конкретному департаменту),
surname (ищет работника по его фамилии). На этой же странице реализована функция добавления сотрудника через метод POST.
Доступ к странице имеют только авторизованные пользователи.
- '/api/worker/<id сотрудника>' - страница конкретного работника. Здесь же реализованы функции изменения информации о 
работники (через методы PUT и PATCH) и удаления работника (через метод DELETE).
- '/api/registration' - страница регистрации новых пользователей.
- '/api/authlogin/' - страница авторизации.

## Установка
1. Скопируйте проект: `git clone https://github.com/sergeytompson/company_test_task`
2. Перейдите в папку проекта: `cd company_test_task`
3. Запустите проект: `docker-compose up`
### Superuser
Для работы с административной частью проекта необходимо авторизаваться на странице '/admin/' с помощью логина
'superuser' и пароля 'superpassword'.

## Фикстуры
Для удобства ознакомления с проектом, при его запуске БД будет автоматически заполнена данными о двух департаментах и 10 
работниках.

## Контакты
+ Telegram: @sergeytompson
+ Email: gfhfahfp@gmail.com