# test_pipeline.py
from pipeline import validate_data

def test_validate_data():
    sample = {"id": 1, "name": "Sensor_A", "value": 23.5}
    assert validate_data(sample) is not None

def test_invalid_data():
    sample = {"id": "not_an_int", "name": "Sensor_B"}
    assert validate_data(sample) is None