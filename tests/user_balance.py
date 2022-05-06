from werkzeug.security import generate_password_hash

from app import User, db
from app.db.models import Transaction


def test_user_balance(application):
    """Tests the user balance calculation"""
    user = User('test@test.com', generate_password_hash('test1234'))
    with application.app_context():
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        user.authenticated = True
        user.transactions = [Transaction(500, "Credit 1"), Transactions(500, "Credit 2")]
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        userid = user.id
        user_trans = Transaction.query.filter_by(user_id=userid).all()
        total = 0
        for trans in user_trans:
            total += trans.amount
        assert total == 1000