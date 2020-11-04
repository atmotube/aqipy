from aqipy import aqhi_hk


def test_get_aqi_ozone_8h():
    aqhi, text1, text2 = aqhi_hk.get_aqhi(0.015, 0, 0, 150, 20)
    assert aqhi == 5
    assert text1 == aqhi_hk.HK_AQHI_GENERAL[1]
    assert text2 == aqhi_hk.HK_AQHI_RISK[1]
    aqhi, text1, text2 = aqhi_hk.get_aqhi(0, 0, 0, 0, 0)
    assert aqhi == 1
