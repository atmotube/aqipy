from aqipy import aqi_au


def test_get_aqi_ozone_8h():
    aqi, text1, text2 = aqi_au.get_aqi_o3_1h(0.07853333)
    assert aqi == 70
    assert text1 == aqi_au.AU_AQI_GENERAL[2]
    assert text2 == aqi_au.AU_AQI_RISK[2]
    aqi, aqi_data = aqi_au.get_aqi(o3_1h=0.07853333)
    assert aqi == 70
    assert aqi_data['o3_1h'][0] == 70
    assert aqi_data['o3_1h'][1] == aqi_au.AU_AQI_GENERAL[2]
    assert aqi_data['o3_1h'][2] == aqi_au.AU_AQI_RISK[2]
    assert aqi_au.get_aqi()[0] == -1
    aqi, aqi_data = aqi_au.get_aqi(o3_1h=0.07853333, co_8h=5)
    assert aqi == 70
    assert 'o3_1h' in aqi_data
    assert 'co_8h' in aqi_data
    assert aqi_data['co_8h'][0] == 56


def test_get_aqi_ozone_8h_with_level():
    aqi, aqi_data = aqi_au.get_aqi(o3_1h=0.07853333, with_level=True)
    assert aqi == 70
    assert aqi_data.get('level') == 'fair'


def test_levels():
    assert len(aqi_au.AU_AQI) == len(aqi_au.AU_AQI_LEVELS)


def test_labels():
    assert len(aqi_au.AU_AQI) == len(aqi_au.AU_AQI_GENERAL)
    assert len(aqi_au.AU_AQI) == len(aqi_au.AU_AQI_RISK)


def test_max():
    aqi, text1, text2 = aqi_au.get_aqi_o3_1h(100)
    assert aqi == 201
    aqi, aqi_data = aqi_au.get_aqi(o3_1h=100)
    assert aqi == 201
    aqi, text1, text2 = aqi_au.get_aqi_o3_1h(0)
    assert aqi == 0


def test_arrays_val():
    aqi(aqi_au.AU_AQI)


def aqi(a:[]):
    a_len = len(a)
    for i in range(a_len):
        if a[i][1] == 0:
            continue
        assert a[i][0] < a[i][1] or i == a_len - 1
        if i < a_len - 1:
            assert a[i][1] < a[i + 1][0]
