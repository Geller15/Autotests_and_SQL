import sender_stand_request
import data
import pytest

def test_get_order_from_track():
    assert sender_stand_request.response.status_code == 200
