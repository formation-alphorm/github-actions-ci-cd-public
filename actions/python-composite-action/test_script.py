import requests

def test_status_code():
    response = requests.get("https://httpbin.org/status/200")
    assert response.status_code == 200

if __name__ == "__main__":
    test_status_code()
    print("All tests passed!")
