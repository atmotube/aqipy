from aqipy import cai_kr


def test_get_aqi_ozone_8h():
    aqi, text1, text2 = cai_kr.get_cai_o3_1h(0.07853333)
    assert aqi == 90
    assert text1 == cai_kr.KR_AQI_GENERAL[1]
    assert text2 == cai_kr.KR_AQI_GENERAL[1]
    aqi, aqi_data = cai_kr.get_aqi(o3_1h=0.07853333)
    assert aqi == 90
    assert aqi_data['o3_1h'][0] == 90
    assert aqi_data['o3_1h'][1] == cai_kr.KR_AQI_GENERAL[1]
    assert aqi_data['o3_1h'][2] == cai_kr.KR_AQI_GENERAL[1]
    assert cai_kr.get_aqi()[0] == -1
    aqi, aqi_data = cai_kr.get_aqi(o3_1h=0.07853333, co_1h=5)
    assert aqi == 90
    assert 'o3_1h' in aqi_data
    assert 'co_1h' in aqi_data
    assert aqi_data['co_1h'][0] == 72


def test_get_aqi_ozone_8h_with_level():
    aqi, aqi_data = cai_kr.get_aqi(o3_1h=0.07853333, with_level=True)
    assert aqi == 90
    assert aqi_data.get('level') == 'moderate'


def test_levels():
    assert len(cai_kr.KR_CAI) == len(cai_kr.KR_CAI_LEVELS)


def test_labels():
    assert len(cai_kr.KR_CAI) == len(cai_kr.KR_AQI_GENERAL)


def test_max():
    aqi, text1, text2 = cai_kr.get_cai_o3_1h(100)
    assert aqi == 500
    aqi, aqi_data = cai_kr.get_aqi(o3_1h=100)
    assert aqi == 500
    aqi, text1, text2 = cai_kr.get_cai_o3_1h(0)
    assert aqi == 0


def test_arrays_val():
    aqi(cai_kr.KR_CAI)
    aqi(cai_kr.KR_O3_1H)
    aqi(cai_kr.KR_CO_1H)
    aqi(cai_kr.KR_SO2_1H)
    aqi(cai_kr.KR_NO2_1H)
    aqi(cai_kr.KR_PM25_24H)
    aqi(cai_kr.KR_PM10_24H)


def aqi(a:[]):
    a_len = len(a)
    for i in range(a_len):
        if a[i][1] == 0:
            continue
        assert a[i][0] < a[i][1] or i == a_len - 1
        if i < a_len - 1:
            assert a[i][1] < a[i + 1][0]
