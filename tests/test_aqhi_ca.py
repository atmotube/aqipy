from aqipy import aqhi_ca


def test_get_aqi_ozone_8h():
    aqhi, text1, text2 = aqhi_ca.get_aqhi(0.015, 0, 100, 20)
    assert aqhi == 6
    assert text1 == aqhi_ca.CA_AQHI_GENERAL[1]
    assert text2 == aqhi_ca.CA_AQHI_RISK[1]
    aqhi, text1, text2 = aqhi_ca.get_aqhi(0, 0, 0, 0)
    assert aqhi == 1

def test_get_aqi_ozone_8h_with_level():
    aqhi, data = aqhi_ca.get_aqhi(0.015, 0, 100, 20, True)
    assert aqhi == 6
    assert data.get('level') == 'moderate'
    aqhi, data = aqhi_ca.get_aqhi(0, 0, 0, 0, True)
    assert aqhi == 1
    assert data.get('level') == 'low'


def test_levels():
    assert len(aqhi_ca.CA_AQHI) == len(aqhi_ca.CA_AQHI_LEVELS)
