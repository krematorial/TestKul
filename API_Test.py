import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import pytest

BASE_URL = "https://rickandmortyapi.com/api"

schema_character = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "status": {"type": "string"},
        "species": {"type": "string"},
        "type": {"type": "string"},
        "gender": {"type": "string"},
        "origin": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "url": {"type": "string"}
            },
            "required": ["name", "url"]
        },
        "location": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "url": {"type": "string"}
            },
            "required": ["name", "url"]
        },
        "image": {"type": "string"},
        "episode": {
            "type": "array",
            "items": {"type": "string"}
        },
        "url": {"type": "string"},
        "created": {"type": "string"}
    },
    "required": ["id", "name", "status", "species", "gender", "origin", "location", "image", "episode", "url",
                 "created"]
}

schema_characters_list = {
    "type": "object",
    "properties": {
        "info": {
            "type": "object",
            "properties": {
                "count": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": ["string", "null"]},
                "prev": {"type": ["string", "null"]}
            },
            "required": ["count", "pages", "next", "prev"]
        },
        "results": {
            "type": "array",
            "items": schema_character
        }
    },
    "required": ["info", "results"]
}

schema_episode = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "air_date": {"type": "string"},
        "episode": {"type": "string"},
        "characters": {
            "type": "array",
            "items": {"type": "string"}
        },
        "url": {"type": "string"},
        "created": {"type": "string"}
    },
    "required": ["id", "name", "air_date", "episode", "characters", "url", "created"]
}

schema_location = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "type": {"type": "string"},
        "dimension": {"type": "string"},
        "residents": {
            "type": "array",
            "items": {"type": "string"}
        },
        "url": {"type": "string"},
        "created": {"type": "string"}
    },
    "required": ["id", "name", "type", "dimension", "residents", "url", "created"]
}

schema_error = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

@pytest.fixture
def base_url():
    return BASE_URL

def print_response(response):
    print("Status Code:", response.status_code)
    try:
        print("Response Body:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response Body: No content (empty body)")
    print("Headers:", response.headers)
    print("Cookies:", response.cookies)
    print("-" * 50)


def test_get_character(base_url):
    character_id = 1  # Рик Санчез
    response = requests.get(f"{base_url}/character/{character_id}")
    print_response(response)
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schema_character)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы персонажа: {e}")


def test_get_characters_list(base_url):
    response = requests.get(f"{base_url}/character")
    print_response(response)
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schema_characters_list)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы списка персонажей: {e}")


def test_get_character_not_found(base_url):
    character_id = 9999  # Несуществующий ID
    response = requests.get(f"{base_url}/character/{character_id}")
    print_response(response)
    assert response.status_code == 404
    try:
        validate(instance=response.json(), schema=schema_error)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы ошибки: {e}")


def test_filter_characters(base_url):
    # Фильтрация по статусу и виду
    response = requests.get(f"{base_url}/character", params={
        "status": "alive",
        "species": "human"
    })
    print_response(response)
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schema_characters_list)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы при фильтрации: {e}")


def test_get_episode(base_url):
    episode_id = 1
    response = requests.get(f"{base_url}/episode/{episode_id}")
    print_response(response)
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schema_episode)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы эпизода: {e}")


def test_get_episodes_list(base_url):
    response = requests.get(f"{base_url}/episode")
    print_response(response)
    assert response.status_code == 200
    # Для списка эпизодов используем схему с results и info
    schema_episodes_list = {
        "type": "object",
        "properties": {
            "info": schema_characters_list["properties"]["info"],
            "results": {
                "type": "array",
                "items": schema_episode
            }
        },
        "required": ["info", "results"]
    }
    try:
        validate(instance=response.json(), schema=schema_episodes_list)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы списка эпизодов: {e}")


def test_get_location(base_url):
    location_id = 1  # Земля (C-137)
    response = requests.get(f"{base_url}/location/{location_id}")
    print_response(response)
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schema_location)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы локации: {e}")


def test_get_locations_list(base_url):
    response = requests.get(f"{base_url}/location")
    print_response(response)
    assert response.status_code == 200
    # Для списка локаций используем схему с results и info
    schema_locations_list = {
        "type": "object",
        "properties": {
            "info": schema_characters_list["properties"]["info"],
            "results": {
                "type": "array",
                "items": schema_location
            }
        },
        "required": ["info", "results"]
    }
    try:
        validate(instance=response.json(), schema=schema_locations_list)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы списка локаций: {e}")


def test_get_multiple_characters(base_url):
    # Запрос нескольких персонажей за раз
    response = requests.get(f"{base_url}/character/[1,2,3]")
    print_response(response)
    assert response.status_code == 200

    # Проверяем что это массив персонажей
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3

    # Валидируем каждого персонажа
    for character in data:
        try:
            validate(instance=character, schema=schema_character)
        except ValidationError as e:
            pytest.fail(f"Ошибка валидации схемы персонажа в массиве: {e}")


def test_search_character(base_url):
    response = requests.get(f"{base_url}/character", params={"name": "rick"})
    print_response(response)
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schema_characters_list)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации схемы при поиске: {e}")

    data = response.json()
    if data["results"]:
        assert any("rick" in character["name"].lower() for character in data["results"])


if __name__ == "__main__":
    print("Запуск тестов Rick and Morty API...")
    import sys

    sys.exit(pytest.main([__file__, "-v"]))