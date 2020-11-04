from aqipy import aqi_cn


def test_get_aqi_ozone_8h():
    aqi, text1, text2 = aqi_cn.get_aqi_o3_8h(0.07853333)
    assert aqi == 97
    assert text1 == aqi_cn.CN_AQI_EFFECTS[1]
    assert text2 == aqi_cn.CN_AQI_CAUTIONS[1]
    aqi, aqi_data = aqi_cn.get_aqi(o3_8h=0.07853333)
    assert aqi == 97
    assert aqi_data['o3_8h'][0] == 97
    assert aqi_data['o3_8h'][1] == aqi_cn.CN_AQI_EFFECTS[1]
    assert aqi_data['o3_8h'][2] == aqi_cn.CN_AQI_CAUTIONS[1]
    assert aqi_cn.get_aqi()[0] == -1
    aqi, aqi_data = aqi_cn.get_aqi(o3_8h=0.07853333, co_24h=2)
    assert aqi == 97
    assert 'o3_8h' in aqi_data
    assert 'co_24h' in aqi_data
    assert aqi_data['co_24h'][0] == 60


def test_labels():
    assert len(aqi_cn.CN_AQI) == len(aqi_cn.CN_AQI_EFFECTS)
    assert len(aqi_cn.CN_AQI) == len(aqi_cn.CN_AQI_CAUTIONS)


def test_max():
    aqi, text1, text2 = aqi_cn.get_aqi_o3_8h(100)
    assert aqi == 300
    aqi, aqi_data = aqi_cn.get_aqi(o3_8h=100)
    assert aqi == 300
    aqi, text1, text2 = aqi_cn.get_aqi_o3_1h(0)
    assert aqi == 0


def test_arrays_val():
    aqi(aqi_cn.CN_AQI)
    aqi(aqi_cn.CN_SO2_24H)
    aqi(aqi_cn.CN_NO2_24H)
    aqi(aqi_cn.CN_CO_24H)
    aqi(aqi_cn.CN_O3_1H)
    aqi(aqi_cn.CN_O3_8H)
    aqi(aqi_cn.CN_PM25_24H)
    aqi(aqi_cn.CN_PM10_24H)


def aqi(a:[]):
    a_len = len(a)
    for i in range(a_len):
        if a[i][1] == 0:
            continue
        assert a[i][0] < a[i][1] or i == a_len - 1
        if i < a_len - 1:
            assert a[i][1] < a[i + 1][0]
