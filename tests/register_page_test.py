"""This tests the registration page"""


def test_register_page(client):
    response = client.get("/register")
    assert response.status_code == 200
