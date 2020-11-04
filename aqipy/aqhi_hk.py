# coding: utf-8

"""
    Hong Kong AQHI
    Source: https://www.aqhi.gov.hk/en/what-is-aqhi/faqs.html
            https://www.aqhi.gov.hk/pdf/related_websites/APIreview_report.pdf
            https://www.gov.hk/en/residents/environment/air/aqhi.htm
"""

import math
from aqipy.utils import AQI_NOT_AVAILABLE, __get_aqi_texts, __added_risk

HK_AR = (
    (0.00, 1.87), (1.88, 3.76), (3.76, 5.63), (5.64, 7.51), (7.52, 9.40), (9.41, 11.28), (11.29, 12.90), (12.91, 15.06),
    (15.07, 17.21), (17.22, 19.36), (19.37, 19.37)
)

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


def get_aqhi(o3_3h: float, no2_3h: float, so2_3h: float, pm25_3h: float, pm10_3h: float) -> (float, str, str):
    """
    Calculates US AQHI

    :param o3_3h: O3 average (3h), ppm
    :param no2_3h: NO2 average (3h), ppm
    :param so2_3h: SO2 average (3h), ppm
    :param pm25_3h: PM2.5 average (3h), μg/m3
    :param pm10_3h: PM10 average (3h), μg/m3
    :return: CA AQHI, Effect message, Caution message
    """
    betas = [0.0004462559, 0.0001393235, 0.0005116328, 0.0002821751, 0.0002180567]
    c = [no2_3h * 1000 * NO2_PPB_UGM3, so2_3h * 1000 * SO2_PPB_UGM3, o3_3h * 1000 * O3_PPB_UGM3, pm10_3h, pm25_3h]
    ars = list(map(__added_risk, betas, c))
    ar_total = sum(ars[0:3]) + max(ars[3:5])
    aqhi = max(1, min(len(HK_AR), round(ar_total)))
    text1, text2 = __get_aqi_texts(aqhi, HK_AR, HK_AQHI_GENERAL, HK_AQHI_RISK)
    return aqhi, text1, text2
