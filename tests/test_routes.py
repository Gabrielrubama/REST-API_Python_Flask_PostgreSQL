#  tests/test_routes.py

def test_get_movies(client):
    response = client.get("/api/movies")
    assert response.status_code == 200
    assert response.content_type == "application/json"

    data = response.get_json()
    assert isinstance(data, list)


def test_get_movie_by_id(client):
    movie_id = 1
    response = client.get(f"/api/movies/{movie_id}")
    assert response.status_code == 200
    assert response.content_type == "application/json"

    data = response.get_json()
    assert isinstance(data, dict)
    assert "title" in data
    assert "director" in data
    assert "year" in data
