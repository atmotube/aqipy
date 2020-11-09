from aqipy import psi_sg


def test_get_psi_ozone_8h():
    aqi, text1, text2 = psi_sg.get_psi_o3_8h(0.07853333)
    assert aqi == 100
    assert text1 == psi_sg.SG_AQI_GENERAL[1]
    assert text2 == psi_sg.SG_AQI_RISK[1]
    aqi, aqi_data = psi_sg.get_aqi(o3_8h=0.07853333)
    assert aqi == 100
    assert aqi_data['o3_8h'][0] == 100
    assert aqi_data['o3_8h'][1] == psi_sg.SG_AQI_GENERAL[1]
    assert aqi_data['o3_8h'][2] == psi_sg.SG_AQI_RISK[1]
    assert psi_sg.get_aqi()[0] == -1
    aqi, aqi_data = psi_sg.get_aqi(o3_8h=0.07853333, co_8h=5)
    assert aqi == 100
    assert 'o3_8h' in aqi_data
    assert 'co_8h' in aqi_data
    assert aqi_data['co_8h'][0] == 57


def test_division_by_zero():
    aqi, aqi_data = psi_sg.get_aqi(no2_1h=0.0001)
    assert aqi
    assert aqi_data


def test_labels():
    assert len(psi_sg.SG_PSI) == len(psi_sg.SG_AQI_GENERAL)
    assert len(psi_sg.SG_PSI) == len(psi_sg.SG_AQI_RISK)


def test_max():
    aqi, text1, text2 = psi_sg.get_psi_o3_8h(100)
    assert aqi == 500
    aqi, aqi_data = psi_sg.get_aqi(o3_8h=100)
    assert aqi == 500
    aqi, text1, text2 = psi_sg.get_psi_o3_8h(0)
    assert aqi == 0


def test_arrays_val():
    aqi(psi_sg.SG_PSI)
    aqi(psi_sg.SG_PM25_24H)
    aqi(psi_sg.SG_PM10_24H)
    aqi(psi_sg.SG_SO2_24H)
    aqi(psi_sg.SG_CO_8H)
    aqi(psi_sg.SG_O3_8H)
    aqi(psi_sg.SG_NO2_1H)


def aqi(a:[]):
    a_len = len(a)
    for i in range(a_len):
        if a[i][1] == 0:
            continue
        assert a[i][0] < a[i][1]
        if i < a_len - 1:
            assert a[i][1] < a[i + 1][0]
