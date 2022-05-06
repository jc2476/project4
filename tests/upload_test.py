import csv
import os

import pytest
import unittest

from pylint.testutils.functional import test_file

from app import db, User
from app.db.models import Transaction


class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir()
        tmpdir.join("music.csv").write("# testdata")

    def test_method(self):
        with open("music.csv") as f:
            s = f.read()
        assert "testdata" in s



def process_csv_test(application):
    with application.app_context:
        db.create_all()
        user = User('joe@joe.com', 'joe123')
        db.session.add(user)
        list_of_transactions = []
        with open(test_file) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_transactions.append(Transaction(row['Amount'], row['Type']))
        user.transactions = list_of_transactions
        db.session.commit()
        test_transaction = Transaction.query.filter_by(amount='2000').first
        assert test_transaction.amount == '2000'
        db.session.delete(user)
        assert db.session.query(user).count() == 0
        os.remove(test_file)
        assert os.path.exists(test_file) == False



