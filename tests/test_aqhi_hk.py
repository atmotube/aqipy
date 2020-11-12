from aqipy import aqhi_hk


def test_get_aqi_none():
    aqhi, text1, text2 = aqhi_hk.get_aqhi(None, None, None, None, None)
    assert aqhi == -1


def test_get_aqi_ozone_8h():
    aqhi, text1, text2 = aqhi_hk.get_aqhi(0.015, 0, 0, 150, 20)
    assert aqhi == 3
    assert text1 == aqhi_hk.HK_AQHI_GENERAL[aqhi - 1]
    assert text2 == aqhi_hk.HK_AQHI_RISK[aqhi - 1]
    aqhi, text1, text2 = aqhi_hk.get_aqhi(0, 0, 0, 0, 0)
    assert aqhi == 1
    aqhi, text1, text2 = aqhi_hk.get_aqhi(0.015, 0.05, 0, 35, 61)
    assert aqhi == 5
