from aqipy import aqi_in


def test_get_aqi_ozone_8h():
    aqi, text1, text2 = aqi_in.get_aqi_o3_8h(0.07853333)
    assert aqi == 223
    assert text1 == aqi_in.IN_AQI_EFFECTS[2]
    assert text2 == aqi_in.IN_AQI_EFFECTS[2]
    aqi, aqi_data = aqi_in.get_aqi(o3_8h=0.07853333)
    assert aqi == 223
    assert aqi_data['o3_8h'][0] == 223
    assert aqi_data['o3_8h'][1] == aqi_in.IN_AQI_EFFECTS[2]
    assert aqi_data['o3_8h'][2] == aqi_in.IN_AQI_EFFECTS[2]
    assert aqi_in.get_aqi()[0] == -1
    aqi, aqi_data = aqi_in.get_aqi(o3_8h=0.07853333, co_8h=5)
    assert aqi == 223
    assert 'o3_8h' in aqi_data
    assert 'co_8h' in aqi_data
    assert aqi_data['co_8h'][0] == 171


def test_get_aqi_ozone_8h_with_level():
    aqi, aqi_data = aqi_in.get_aqi(o3_8h=0.07853333, with_level=True)
    assert aqi == 223
    assert aqi_data.get('level') == 'moderately polluted'


def test_levels():
    assert len(aqi_in.IN_AQI) == len(aqi_in.IN_AQI_LEVELS)


def test_labels():
    assert len(aqi_in.IN_AQI) == len(aqi_in.IN_AQI_EFFECTS)


def test_max():
    aqi, text1, text2 = aqi_in.get_aqi_o3_8h(100)
    assert aqi == 500
    aqi, aqi_data = aqi_in.get_aqi(o3_8h=100)
    assert aqi == 500
    aqi, text1, text2 = aqi_in.get_aqi_o3_8h(0)
    assert aqi == 0


def test_arrays_val():
    aqi(aqi_in.IN_AQI)
    aqi(aqi_in.IN_O3_8H)
    aqi(aqi_in.IN_PM25_24H)
    aqi(aqi_in.IN_PM10_24H)
    aqi(aqi_in.IN_CO_8H)
    aqi(aqi_in.IN_SO2_24H)
    aqi(aqi_in.IN_NO2_24H)
    aqi(aqi_in.IN_NH3_24H)
    aqi(aqi_in.IN_PB_24H)


def aqi(a:[]):
    a_len = len(a)
    for i in range(a_len):
        if a[i][1] == 0:
            continue
        assert a[i][0] < a[i][1] or i == a_len - 1
        if i < a_len - 1:
            assert a[i][1] < a[i + 1][0]
