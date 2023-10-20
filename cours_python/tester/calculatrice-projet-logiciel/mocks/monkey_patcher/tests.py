from mocks import source


def test_main_function(monkeypatch):
    def mockreturn():
        return 100

    monkeypatch.setattr(source, 'request', mockreturn)

    expected_value = 100
    assert source.main_function() == expected_value


class MockResponse:
    @staticmethod
    def get_info():
        return {"name": "test", "level": 200}


def test_create_player(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr('mocks.source.Player', mock_get)

    expected_value = {"name": "test", "level": 200}
    assert source.create_player() == expected_value
