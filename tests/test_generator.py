from honeytoken_service.generator import generate_api_key, fake_user, fake_db_row


def test_api_key_length():
    key = generate_api_key()
    assert key.startswith("ht_")
    assert len(key) > 10


def test_fake_user_fields():
    u = fake_user()
    assert "username" in u and "email" in u


def test_db_row():
    row = fake_db_row()
    assert row.get("table") == "customers"
