from aqipy import caqi_eu


def test_get_caqi_ozone_8h():
    caqi = caqi_eu.get_caqi_o3_1h(0.07853333)
    assert caqi == 65
    caqi, aqi_data = caqi_eu.get_caqi(o3_max_1h=0.07853333)
    assert caqi == 65
    assert aqi_data['o3_1h'] == 65
    assert caqi_eu.get_caqi()[0] == -1
    aqi, aqi_data = caqi_eu.get_caqi(o3_max_1h=0.07853333, co_1h=5)
    assert aqi == 65
    assert 'o3_1h' in aqi_data
    assert 'co_1h' in aqi_data
    assert aqi_data['co_1h'] == 32


def test_max():
    aqi = caqi_eu.get_caqi_o3_1h(100)
    assert aqi == 100
    aqi, aqi_data = caqi_eu.get_caqi(o3_max_1h=100)
    assert aqi == 100
    aqi = caqi_eu.get_caqi_o3_1h(100)
    assert aqi == 100
    aqi = caqi_eu.get_caqi_o3_1h(0)
    assert aqi == 0


def test_arrays_val():
    aqi(caqi_eu.EU_CAQI)
    aqi(caqi_eu.EU_NO2_1H)
    aqi(caqi_eu.EU_PM10_1H)
    aqi(caqi_eu.EU_PM10_24H)
    aqi(caqi_eu.EU_PM25_1H)
    aqi(caqi_eu.EU_PM25_24H)
    aqi(caqi_eu.EU_O3_1H)
    aqi(caqi_eu.EU_CO_8H)
    aqi(caqi_eu.EU_SO2_1H)


def aqi(a: []):
    a_len = len(a)
    for i in range(a_len):
        if a[i][1] == 0:
            continue
        assert a[i][0] < a[i][1] or i == a_len - 1
        if i < a_len - 1:
            assert a[i][1] < a[i + 1][0]
