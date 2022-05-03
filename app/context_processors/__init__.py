from os import getenv
import datetime

import sqlalchemy
from flask_login import current_user
from sqlalchemy.sql import func
from app import transactions
from app.auth.forms import login_form



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
        engine = sqlalchemy.create_engine("sqlite:////home/myuser/database/db2.sqlite")
        data = sqlalchemy.MetaData(bind=engine)
        sqlalchemy.MetaData.reflect(data)
        #user = current_user
        total = data.tables['transactions']
        query = sqlalchemy.select(sqlalchemy.func.sum(total.c.amount))
        result = engine.execute(query).fetchall()
        currency = str(result[0])
        balance = currency[1:-2]
        return "${:,.2f}".format(float(balance))

    return dict(
        form=form,
        mymessage=message,
        deployment_environment=deployment_environment(),
        year=current_year(),
        format_price=format_price,
        bank_balance=bank_balance()

    )
