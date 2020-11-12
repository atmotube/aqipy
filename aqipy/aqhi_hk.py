# coding: utf-8

"""
    Hong Kong AQHI
    Source: https://www.aqhi.gov.hk/en/what-is-aqhi/faqs.html
            https://www.aqhi.gov.hk/pdf/related_websites/APIreview_report.pdf
            https://www.gov.hk/en/residents/environment/air/aqhi.htm
"""

from typing import Union, Tuple

from aqipy.utils import AQI_NOT_AVAILABLE, __get_aqi_texts, __added_risk, __get_aqi_level

HK_AR = (
    (0.00, 1.87), (1.88, 3.76), (3.76, 5.63), (5.64, 7.51), (7.52, 9.40), (9.41, 11.28), (11.29, 12.90), (12.91, 15.06),
    (15.07, 17.21), (17.22, 19.36), (19.37, 19.37)
)

HK_AQHI = ((1, 3), (4, 6), (7, 7), (8, 10), (11, 11))
HK_AQHI_LEVELS = ('low', 'moderate', 'high', 'very high', 'serious')

HK_AQHI_GENERAL = (
    "No response action is required.",
    "No response action is required.",
    "No response action is required.",
    "No response action is required.",
    "No response action is required.",
    "No response action is required.",
    "No response action is required.",
    "The general public is advised to reduce outdoor physical exertion, and to reduce the time of their stay outdoors, especially in areas with heavy traffic.",
    "The general public is advised to reduce outdoor physical exertion, and to reduce the time of their stay outdoors, especially in areas with heavy traffic.",
    "The general public is advised to reduce outdoor physical exertion, and to reduce the time of their stay outdoors, especially in areas with heavy traffic.",
    "The general public is advised to reduce to the minimum outdoor physical exertion, and to reduce to the minimum the time of their stay outdoors, especially in areas with heavy traffic."
)
# People with existing heart or respiratory illnesses
HK_AQHI_RISK = (
    "No response action is required.",
    "No response action is required.",
    "No response action is required.",
    "No response action is normally required. Individuals who are experiencing symptoms are advised to consider reducing outdoor physical exertion.",
    "No response action is normally required. Individuals who are experiencing symptoms are advised to consider reducing outdoor physical exertion.",
    "No response action is normally required. Individuals who are experiencing symptoms are advised to consider reducing outdoor physical exertion.",
    "People with existing heart or respiratory illnesses are advised to reduce outdoor physical exertion, and to reduce the time of their stay outdoors, especially in areas with heavy traffic. They should also seek advice from a medical doctor before participating in sport activities and take more breaks during physical activities.",
    "People with existing heart or respiratory illnesses are advised to reduce to the minimum outdoor physical exertion, and to reduce to the minimum the time of their stay outdoors, especially in areas with heavy traffic.",
    "People with existing heart or respiratory illnesses are advised to reduce to the minimum outdoor physical exertion, and to reduce to the minimum the time of their stay outdoors, especially in areas with heavy traffic.",
    "People with existing heart or respiratory illnesses are advised to reduce to the minimum outdoor physical exertion, and to reduce to the minimum the time of their stay outdoors, especially in areas with heavy traffic.",
    "People with existing heart or respiratory illnesses are advised to avoid outdoor physical exertion, and to avoid staying outdoors, especially in areas with heavy traffic."
)

NO2_PPB_UGM3 = 1.88
SO2_PPB_UGM3 = 2.62
O3_PPB_UGM3 = 2


def get_aqhi(o3_3h: float, no2_3h: float, so2_3h: float, pm25_3h: float, pm10_3h: float, with_level: bool = False) -> \
        Union[Tuple[int, str, str], Tuple[int, dict]]:
    """
    Calculates Hong Kong AQHI

    :param o3_3h: O3 average (3h), ppm
    :param no2_3h: NO2 average (3h), ppm
    :param so2_3h: SO2 average (3h), ppm
    :param pm25_3h: PM2.5 average (3h), μg/m3
    :param pm10_3h: PM10 average (3h), μg/m3
    :param with_level: Boolean distinguishing whether to print AQI level such as 'good' or 'hazardous'
    :return: Hong Kong AQHI, Effect message, Caution message
    """
    if any(value is None for value in (o3_3h, no2_3h, so2_3h, pm10_3h, pm25_3h)):
        return AQI_NOT_AVAILABLE, "", ""
    betas = [0.0004462559, 0.0001393235, 0.0005116328, 0.0002821751, 0.0002180567]
    if so2_3h == 0:
        so2_3h = 0.020  # normal level - to make formula work without SO2
    c = [no2_3h * 1000 * NO2_PPB_UGM3, so2_3h * 1000 * SO2_PPB_UGM3, o3_3h * 1000 * O3_PPB_UGM3, pm10_3h, pm25_3h]
    ars = list(map(__added_risk, betas, c))
    ar_total = sum(ars[0:3]) + max(ars[3:5])
    aqhi = len(HK_AR)
    for i in range(len(HK_AR)):
        if HK_AR[i][0] <= ar_total <= HK_AR[i][1]:
            aqhi = i + 1
    text1, text2 = __get_aqi_texts(aqhi, HK_AR, HK_AQHI_GENERAL, HK_AQHI_RISK)
    if not with_level:
        return aqhi, text1, text2
    return aqhi, {'level': __get_aqi_level(aqhi, HK_AQHI, HK_AQHI_LEVELS)}
