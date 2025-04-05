from fastapi.testclient import TestClient
from API.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Celare API is running!"}


def test_anonymize_text_valid():
    response_1 = client.post(
        "/v1/anonymize",
        json={"content": ""},
    )
    response_2 = client.post(
        "/v1/anonymize",
        json={"content": " "},
    )

    assert response_1.json() == {'error': '400: No valid text provided'}
    assert response_2.json() == {'error': '400: No valid text provided'}


def test_anonymize_text_valid_length():
    response_1 = client.post(
        "/v1/anonymize",
        json={"content": "aaaaaaaa"},
    )
    response_2 = client.post(
        "/v1/anonymize",
        json={"content": "a" * 501},
    )

    assert response_1.json() == {'error': '400: Text length must be between 10 and 500 characters'}
    assert response_2.json() == {'error': '400: Text length must be between 10 and 500 characters'}


def test_anonymize_text_with_no_sensitive_content():
    response = client.post(
        "/v1/anonymize",
        json={"content": "This is a test text with no info."}
    )

    assert response.json() == {'error': '400: No sensitive information found to anonymize'}


def test_anonymize_text_valid_anonymization():
    response = client.post(
        "/v1/anonymize",
        json={"content": "This is a test text with Alice and alice@email.com."}
    )

    assert response.json() == {'anonymized_text': 'This is a test text with <PERSON> and <EMAIL>.'}