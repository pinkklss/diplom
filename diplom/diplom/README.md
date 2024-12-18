# Дипломная работа к профессии Python-разработчик «API Сервис заказа товаров для розничных сетей».

## Описание

С увеличением объема торговли и растущей конкуренцией на рынке, работа розничных сетей становится все более зависимой от эффективности взаимодействия с поставщиками. Актуальной задачей является автоматизация процессов заказа товаров. Настоящая работа посвящена разработке API сервиса, который упростит и ускорит эти процессы с использованием технологий Python.


### Необходимо разработать backend-часть (Django) сервиса заказа товаров для розничных сетей.

Определить требования к сервису. Понять, какие функции и возможности должны быть включены в сервис, например, управление товарами, заказами, пользователями, платежами и т.д.
Настроить базу данных. Создать и настроить базу данных для хранения информации о товарах, заказах, пользователях и других сущностях.


### Исходные данные
 
1. Функциональные требования.
2. Информация о товарах: название, описание, цена, количество в наличии. 
3. Документация по API: описание методов API.


## Этапы разработки

Разработку Backend рекомендуется разделить на следующие этапы:

Базовая часть:
1. Создание базы данных.
2. Проработка моделей данных
3. Реализация бизнес-логики.
Написание кода для обработки заказов, управления пользователями, платежей и других функций.
4. Внедрение механизмов аутентификации и авторизации.
5. Реализация API views
6. Полностью готовый backend


Настоятельно рекомендуется вести разработку с использованием git (github/gitlab/bitbucket) с регулярными коммитами в репозиторий, доступный вашему дипломному руководителю. Старайтесь делать коммиты как можно чаще для того, чтобы иметь возможность оперативно получать обратную связь от руководителя проекта и избежать лишнего переписывания кода, если что-то потребует корректировки.

Разберём подробно каждый этап.

### Этап 1. Создание базы данных.

Критерии достижения:

1. Вы имеете актуальный код данного репозитория на рабочем компьютере;
2. У вас создан django-проект и он запускается без ошибок.


### Этап 2. Проработка моделей данных

Критерии достижения:

1. Созданы модели и их дополнительные методы.


### Этап 3. Реализация бизнес-логики

Критерии достижения:

1. Написание кода для обработки заказов, управления пользователями, платежей.


### Этап 4. Внедрение механизмов аутентификации и авторизации.

Критерии достижения:

1. пользователь может авторизироваться

### Этап 5. Реализация forms и views

Критерии достижения:

1. Реализованы API Views для основных страниц сервиса (без админки):
   - Вход
   - Регистрация
   - Список товаров
   - Карточка товара
   - Корзина
   - Подтверждение заказа
   - Спасибо за заказ
   - Заказы
   - Заказ


### Этап 6. Полностью готовый backend

Критерии достижения:

1. Полностью работающие API Endpoint
2. Корректно отрабатывает следующий сценарий:
   - пользователь может авторизироваться;
   - есть возможность отправки данных для регистрации и получения email с подтверждением регистрации;
   - пользователь может подтверждать заказ с вводом адреса доставки;
   - пользователь получает email с подтверждением после ввода адреса доставки;
   - Пользователь может переходить на страницу "Заказы" и открывать созданный заказ.

---