def test_sayfa_aciliyor():
    from app import app
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
