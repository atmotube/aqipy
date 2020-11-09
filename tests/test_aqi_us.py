from aqipy import aqi_us


def test_get_aqi_ozone_8h():
    aqi, text1, text2 = aqi_us.get_aqi_o3_8h(0.07853333)
    assert aqi == 126
    assert text1 == aqi_us.US_OZONE_EFFECTS[2]
    assert text2 == aqi_us.US_OZONE_CAUTIONS[2]
    aqi, aqi_data = aqi_us.get_aqi(o3_8h=0.07853333)
    assert aqi == 126
    assert aqi_data['o3_8h'][0] == 126
    assert aqi_data['o3_8h'][1] == aqi_us.US_OZONE_EFFECTS[2]
    assert aqi_data['o3_8h'][2] == aqi_us.US_OZONE_CAUTIONS[2]
    assert aqi_us.get_aqi()[0] == -1
    aqi, aqi_data = aqi_us.get_aqi(o3_8h=0.07853333, co_8h=5)
    assert aqi == 126
    assert 'o3_8h' in aqi_data
    assert 'co_8h' in aqi_data
    assert aqi_data['co_8h'][0] == 56


def test_division_by_zero():
    aqi, aqi_data = aqi_us.get_aqi(o3_1h=0.0001)
    assert aqi == -1


def test_labels():
    assert len(aqi_us.US_AQI) == len(aqi_us.US_OZONE_EFFECTS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_OZONE_CAUTIONS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_PM_EFFECTS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_PM_CAUTIONS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_CO_EFFECTS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_CO_CAUTIONS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_SO2_EFFECTS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_SO2_CAUTIONS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_NO2_EFFECTS)
    assert len(aqi_us.US_AQI) == len(aqi_us.US_NO2_CAUTIONS)


def test_max():
    aqi, text1, text2 = aqi_us.get_aqi_o3_8h(100)
    assert aqi == 300
    aqi, aqi_data = aqi_us.get_aqi(o3_8h=100)
    assert aqi == 300
    aqi, text1, text2 = aqi_us.get_aqi_o3_1h(100)
    assert aqi == 500
    aqi, text1, text2 = aqi_us.get_aqi_o3_1h(0.1)
    assert aqi == 0


def test_arrays_val():
    aqi(aqi_us.US_AQI)
    aqi(aqi_us.US_OZONE_8H)
    aqi(aqi_us.US_OZONE_1H)
    aqi(aqi_us.US_PM25_24H)
    aqi(aqi_us.US_PM10_24H)
    aqi(aqi_us.US_CO_8H)
    aqi(aqi_us.US_SO2_1H)
    aqi(aqi_us.US_SO2_24H)
    aqi(aqi_us.US_NO2_1H)


def aqi(a:[]):
    a_len = len(a)
    for i in range(a_len):
        if a[i][1] == 0:
            continue
        assert a[i][0] < a[i][1]
        if i < a_len - 1:
            assert a[i][1] < a[i + 1][0]
