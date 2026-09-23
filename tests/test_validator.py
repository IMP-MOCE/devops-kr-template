from validator import validate_email, validate_phone, validate_snils

def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid") is False

def test_validate_phone():
    assert validate_phone("+79991234567") is True
    assert validate_phone("89991234567") is False
    assert validate_phone("+7999123") is False

def test_validate_phone_formatting():
    assert validate_phone("+7 999-123-45-67") is True
    assert validate_phone("79991234567") is True
    assert validate_phone("+79991234567abc") is False

def test_validate_snils():
    assert validate_snils("112-233-445 95") is True
    assert validate_snils("11223344500") is False
    assert validate_snils("123") is False

def test_instructor_snils_cases():
    assert validate_snils("11223344595") is True
    assert validate_snils("001-001-999 65") is True
    assert validate_snils("001-001-999 32") is False
    assert validate_snils("123456789012") is False
    assert validate_snils("abcdefghijk") is False
