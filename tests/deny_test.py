"""This tests that access is denied to users not logged in"""


def test_deny_access(client):
    response = client.get("/browse_songs")
    assert response.status_code == 404


def test_deny_upload(client):
    response = client.get("/songs/upload", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data
