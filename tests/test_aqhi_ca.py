from aqipy import aqhi_ca


def test_get_aqi_ozone_8h():
    aqhi, text1, text2, aqi_data = aqhi_ca.get_aqhi(0.015, 0, 100, 20)
    assert aqhi == 6
    assert text1 == aqhi_ca.CA_AQHI_GENERAL[1]
    assert text2 == aqhi_ca.CA_AQHI_RISK[1]
    assert 'pm25_3h' in aqi_data
    assert 'pm10_3h' in aqi_data
    assert aqi_data['pm25_3h'] == aqhi
    assert aqi_data['pm10_3h'] == 1
    aqhi, text1, text2, aqi_data = aqhi_ca.get_aqhi(0, 0, 0, 0)
    assert aqhi == 1

