import os
from os import getenv
import datetime

import sqlalchemy
from flask import request
from flask_login import current_user
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func, functions
from app import transactions
from app.db.models import Transaction
from app.auth.forms import login_form
from app.db.models import Transaction, User


def utility_text_processors():
    message = "hello world"
    form = login_form()

    def deployment_environment():
        return getenv('FLASK_ENV', None)

    def current_year():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return year

    def format_price(amount, currency="$"):
        return f"{currency}{amount:.2f}"

    def bank_balance():
        try:
            engine = sqlalchemy.create_engine("sqlite:////home/myuser/database/db2.sqlite")
            data = sqlalchemy.MetaData(bind=engine)
            sqlalchemy.MetaData.reflect(data)
            total = data.tables['transactions']
            query = sqlalchemy.select([sqlalchemy.func.round(sqlalchemy.func.sum(total.c.amount), 1)])
            query = query.where(total.c.user_id == current_user.id)
            result = engine.execute(query).fetchall()
            currency = str(result[0])
            balance = currency[1:-2]
            return "${:,.2f}".format(float(balance))
        except:
            return ("$0.00")
    # def bank_balance():
    #     try:
    #         userid = current_user.id
    #         user_trans = Transaction.query.filter_by(user_id=userid).all()
    #         total = 0
    #         for trans in user_trans:
    #             total += trans.amount
    #         return "${:,.2f}".format(float(total))
    #     except:
    #         return AttributeError

    def total_balance():
        try:
            engine = sqlalchemy.create_engine("sqlite:////home/myuser/database/db2.sqlite")
            data = sqlalchemy.MetaData(bind=engine)
            sqlalchemy.MetaData.reflect(data)
            total = data.tables['transactions']
            query = sqlalchemy.select([sqlalchemy.func.round(sqlalchemy.func.sum(total.c.amount), 1)])
            result = engine.execute(query).fetchall()
            currency = str(result[0])
            balance = currency[1:-2]
            return "${:,.2f}".format(float(balance))
        except:
            return ("$0.00")

    return dict(
        form=form,
        mymessage=message,
        deployment_environment=deployment_environment(),
        year=current_year(),
        format_price=format_price,
        bank_balance=bank_balance(),
        total_balance=total_balance()
           )
