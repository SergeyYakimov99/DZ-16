Создали модели под следующую задачу:

- Есть пользователь, он может быть как заказчиком, так и исполнителем.
- Пользователь с ролью Заказчик может создать Заказ.
- Пользователь с ролью Исполнитель может откликнуться на Заказ и предложить выполнить его (Offer).

Заполнили модели, используя исходные данные.

Создали представление для пользователей, заказов и предложений, которые обрабатывают GET-запросы получения всех и одного по идентификатору.

Реализовали создание новой записи в каждой модели посредством метода POST на URL.
Реализовали обновление записи в каждой модели посредством метода PUT на URL. В Body будет приходить JSON со всеми полями для обновление заказа.
Реализовали удаление записи в каждой модели посредством метода DELETE на URL.