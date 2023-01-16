from testpy.bank import is_bank


def test_is_bank():
    assert is_bank('Киви') == 'Yes!!! Is good bank!!!'


def test_is_bank():
    assert is_bank('ПСБ') == 'Yes!!! Is good bank!!!'


def test_is_bank():
    assert is_bank('Сбербанк') == 'OOO!!!((( no popular bank...'