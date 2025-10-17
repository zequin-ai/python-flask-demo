import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "app"))

from application import application

def test_home_route():
    client = application.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello from Flask" in resp.data
