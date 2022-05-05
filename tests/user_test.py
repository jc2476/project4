import logging

from app import db
from app.db.models import User, Transaction


def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        #showing how to add a record
        #create a record
        user = User('test@test.com', 'test123', is_admin=1)
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='test@test.com').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'test@test.com'
        #this is how you get a related record ready for insert
        user.transactions= [Transaction(200,"DEBIT"),Transaction(100,"CREDIT")]
        #commit is what saves the songs
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        trans1 = Transaction.query.filter_by(type='DEBIT').first()
        assert trans1.type == "DEBIT"
        db.session.commit()
        trans2 = Transaction.query.filter_by(type='CREDIT').first()
        assert trans2.type == "CREDIT"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
