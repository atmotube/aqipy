from aqipy import daqi_uk


def test_get_caqi_ozone_8h():
    caqi, text1, text2 = daqi_uk.get_daqi_o3_1h(0.07853333)
    assert caqi == 6
    assert text1 == daqi_uk.UK_DAQI_GENERAL[5]
    assert text2 == daqi_uk.UK_DAQI_RISK[5]
    caqi, aqi_data = daqi_uk.get_daqi(o3_1h=0.07853333)
    assert caqi == 6
    assert aqi_data['o3_1h'][0] == 6
    assert daqi_uk.get_daqi()[0] == -1
    aqi, aqi_data = daqi_uk.get_daqi(o3_1h=0.07853333, pm25_24h=5)
    assert aqi == 6
    assert 'o3_1h' in aqi_data
    assert 'pm25_24h' in aqi_data
    assert aqi_data['pm25_24h'][0] == 1


def test_max():
    aqi, text1, text2 = daqi_uk.get_daqi_o3_1h(10)
    assert aqi == 10
    aqi, aqi_data = daqi_uk.get_daqi(o3_1h=100)
    assert aqi == 10
    aqi, text1, text2 = daqi_uk.get_daqi_o3_1h(100)
    assert aqi == 10
    aqi, text1, text2 = daqi_uk.get_daqi_o3_1h(0)
    assert aqi == 1


def test_arrays_val():
    aqi(daqi_uk.UK_O3_1H)
    aqi(daqi_uk.UK_NO2_1H)
    aqi(daqi_uk.UK_SO2_15M)
    aqi(daqi_uk.UK_PM25_24H)
    aqi(daqi_uk.UK_PM10_24H)


def aqi(a: []):
    a_len = len(a)
    for i in range(a_len):
        if a[i][1] == 0:
            continue
        assert a[i][0] < a[i][1] or i == a_len - 1
        if i < a_len - 1:
            assert a[i][1] < a[i + 1][0]
