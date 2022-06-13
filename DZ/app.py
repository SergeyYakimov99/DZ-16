from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)


@app.route("/users", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        user_data = User.query.all()
        rez = []
        for user in user_data:
            rez.append(user.to_dict())
        return jsonify(rez)
    if request.method == 'POST':
        user = json.loads(request.data)
        new_user = User(
            id=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            age=user['age'],
            email=user['email'],
            role=user['role'],
            phone=user['phone']
        )
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        return "Пользователь создан в БД"


@app.route("/users/<int:sid>", methods=['GET', 'PUT', 'DELETE'])
def get_users_id(sid):
    if request.method == 'GET':
        """ Вывод определенного пользователя"""
        user = User.query.get(sid)
        if user is None:
            return "Такой пользователь не найден"
        else:
            return jsonify(user.to_dict())
    elif request.method == 'PUT':
        """ Изменение определенного пользователя"""
        user_data = json.loads(request.data)
        user = db.session.query(User).get(sid)
        if user is None:
            return "Такой пользователь не найден"
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']
        db.session.add(user)
        db.session.commit()
        db.session.close()
        return f"Пользователь с  id: {sid} изменен"
    elif request.method == 'DELETE':
        """ Удаление определенного пользователя"""
        user = db.session.query(User).get(sid)
        if user is None:
            return "Такой пользователь не найден"
        db.session.delete(user)
        db.session.commit()
        db.session.close()
        return f"Пользователь с  id: {sid} удален"


@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        user_data = Order.query.all()
        rez = []
        for order in user_data:
            rez.append(order.to_dict())
        return jsonify(rez)

    if request.method == 'POST':
        order = json.loads(request.data)
        new_order = Order(
            id=order['id'],
            name=order['name'],
            description=order['description'],
            start_date=order['start_date'],
            end_date=order['end_date'],
            address=order['address'],
            price=order['price'],
            customer_id=order['customer_id'],
            executor_id=order['executor_id']
        )
        db.session.add(new_order)
        db.session.commit()
        db.session.close()
        return "Заказ создан в БД"


@app.route("/orders/<int:sid>", methods=['GET', 'PUT', 'DELETE'])
def get_order_id(sid):
    if request.method == 'GET':
        order = Order.query.get(sid)
        if order is None:
            return "Такой заказ не найден"
        else:
            return jsonify(order.to_dict())
    elif request.method == 'PUT':
        """ Изменение определенного пользователя"""
        order_data = json.loads(request.data)
        order = db.session.query(Order).get(sid)
        if order is None:
            return "Такой заказ не найден"
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.address = order_data['address']
        order.price = order_data['price']
        order.customer_id = order_data['customer_id']
        order.executor_id = order_data['executor_id']
        db.session.add(order)
        db.session.commit()
        db.session.close()
        return f"заказ с  id: {sid} изменен"
    elif request.method == 'DELETE':
        """ Удаление определенного заказа"""
        order = db.session.query(Order).get(sid)
        if order is None:
            return "Такой заказ не найден"
        db.session.delete(order)
        db.session.commit()
        db.session.close()
        return f"заказ с  id: {sid} удален"


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        user_data = Offer.query.all()
        res = []
        for offer in user_data:
            res.append(offer.to_dict())
        return jsonify(res)

    if request.method == 'POST':
        offer = json.loads(request.data)
        new_offer = Offer(
            id=offer['id'],
            order_id=offer['order_id'],
            executor_id=offer['executor_id']
        )
        db.session.add(new_offer)
        db.session.commit()
        db.session.close()
        return "Предложение создано в БД"


@app.route("/offers/<int:sid>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_id(sid):
    if request.method == 'GET':
        offer = Offer.query.get(sid)
        if offer is None:
            return "Такое предложение не найдено"
        else:
            return jsonify(offer.to_dict())
    elif request.method == 'PUT':
        """ Изменение определенного предложения"""
        offer_data = json.loads(request.data)
        offer = db.session.query(Offer).get(sid)
        if offer is None:
            return "Такое предложение не найдено"
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']
        db.session.add(offer)
        db.session.commit()
        db.session.close()
        return f"предложение с  id: {sid} измененo"
    elif request.method == 'DELETE':
        """ Удаление определенного заказа"""
        offer = db.session.query(Offer).get(sid)
        if offer is None:
            return "Такое предложение не найденo"
        db.session.delete(offer)
        db.session.commit()
        db.session.close()
        return f"предложение с  id: {sid} удаленo"


if __name__ == '__main__':
    app.run()
