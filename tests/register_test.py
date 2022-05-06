"""New registration test"""
from app import User, db


def test_register(client):
    """ POST to /register """
    new_email = 'joe@joe.com'
    new_password = 'test123'
    data = {
        'email' : new_email,
        'password' : new_password,
        'confirm' : new_password
    }
    resp = client.post('register', data=data)

    assert resp.status_code == 302

    # verify new user is in database
    new_user = User.query.filter_by(email=new_email).first()
    assert new_user.email == new_email

    db.session.delete(new_user) # pylint: disable=no-member
