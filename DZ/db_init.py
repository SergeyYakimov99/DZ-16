from models import *
import data

""" Создание таблиц и добавление данных в них"""

db.drop_all()
db.create_all()

for user in data.USERS:
    db.session.add(User(
        id=user['id'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        age=user['age'],
        email=user['email'],
        role=user['role'],
        phone=user['phone']
    ))


for order in data.ORDERS:
    db.session.add(Order(
        id=order['id'],
        name=order['name'],
        description=order['description'],
        start_date=order['start_date'],
        end_date=order['end_date'],
        address=order['address'],
        price=order['price'],
        customer_id=order['customer_id'],
        executor_id=order['executor_id']
    ))


for offer in data.OFFERS:
    db.session.add(Offer(
        id=offer['id'],
        order_id=offer['order_id'],
        executor_id=offer['executor_id']
    ))

db.session.commit()
