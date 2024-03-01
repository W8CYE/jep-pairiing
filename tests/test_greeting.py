from greeting import greeting


def test_greeting_given_josh_returns_hello_josh():
    assert greeting("Josh") == "Hello Josh!"


def test_greeting_given_jim_returns_hello_jim():
    assert greeting("Jim") == "Hello Jim!"


def test_greeting_given_world_returns_hello_world():
    assert greeting("World") == "Hello World!"
