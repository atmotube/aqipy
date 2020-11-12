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


def test_get_aqi_ozone_8h_with_level():
    aqhi, data = aqhi_hk.get_aqhi(0.015, 0, 0, 150, 20, with_level=True)
    assert aqhi == 3
    assert data.get('level') == 'low'
    aqhi, data = aqhi_hk.get_aqhi(0, 0, 0, 0, 0, with_level=True)
    assert aqhi == 1
    assert data.get('level') == 'low'
    aqhi, data = aqhi_hk.get_aqhi(0.015, 0.05, 0, 35, 61, with_level=True)
    assert aqhi == 5
    assert data.get('level') == 'moderate'
    aqhi, data = aqhi_hk.get_aqhi(0.15, 0.5, 0.5, 35, 61, with_level=True)
    assert aqhi == 11
    assert data.get('level') == 'serious'
