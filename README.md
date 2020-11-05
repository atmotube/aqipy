# AQI calculation library (python)
[![PyPI version](https://badge.fury.io/py/aqipy-atmotech.svg)](https://badge.fury.io/py/aqipy-atmotech)
[![pypi supported versions](https://img.shields.io/pypi/pyversions/aqipy-atmotech.svg)](https://pypi.python.org/pypi/aqipy-atmotech)

The library calculates the following indexes:
- AQI (US)
- AQHI (Canada)
- CAQI (Europe)
- DAQI (UK)
- AQI (Australia)
- CAI (South Korea)
- PSI (Singapore)
- AQHI (Hong Kong)
- AQI (Mainland China)
- AQI (India)

## Installation

From source:

```
git clone --recursive https://github.com/atmotube/aqipy.git
cd python
python setup.py install
```

From [PyPI](https://pypi.python.org/pypi/aqipy-atmotech/) directly:

```
pip3 install aqipy-atmotech
```

## Examples

calculate US AQI:

```python
from aqipy import aqi_us

aqi, aqi_data = aqi_us.get_aqi(o3_8h=0.07853333, co_8h=5)
print('AQI:', aqi)
print('AQI O3:', aqi_data['o3_8h'][0])
print('Effects O3:', aqi_data['o3_8h'][1])
print('Cautions O3:', aqi_data['o3_8h'][2])
print('AQI CO:', aqi_data['co_8h'][0])
print('Effects CO:', aqi_data['co_8h'][1])
print('Cautions CO:', aqi_data['co_8h'][2])
```

output will be:
```
AQI: 126
AQI O3: 126
Effects O3: Increasing likelihood of respiratory symptoms and breathing discomfort in people with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients.
Cautions O3: People with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients should reduce prolonged or heavy outdoor exertion.
AQI CO: 56
Effects CO:
Cautions CO:
```

## Units
| Pollutant          | Units           |
|--------------------|-----------------|
| CO                 |ppm              |
| O<sub>3</sub>      |ppm              |
| NO<sub>2</sub>     |ppm              |
| SO<sub>2</sub>     |ppm              |
| NH<sub>3</sub>     |ppm              |
| Pb                 |ppm              |
| PM<sub>2.5</sub>   |μg/m<sup>3</sup> |
| PM<sub>10</sub>    |μg/m<sup>3</sup> |

## Summary (averages)
| Index               |PM<sub>2.5</sub> | PM<sub>10</sub> |O<sub>3</sub>     |NO<sub>2</sub>   |CO               |SO<sub>2</sub>   |NH<sub>3</sub>   |Pb               |
|---------------------|-----------------|-----------------|------------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| AQI (US)            |24h              |24h              |8h/1h	         |1h	           |8h               |1h               |-                |-                |
| AQHI (Canada)       |3h	            |3h	              |3h                |3h               |-	             |-	               |-	             |-                |
| CAQI (Europe)       |1h/24h           |1h/24h           |max in 1h         |max in 1h	       |8h	             |max in 1h        |-	             |-                |
| DAQI (UK)           |24h	            |24h	          |8h                |1h	           |-	             |15m              |-	             |-                |
| AQI (Australia)     |24h	            |24h              |1h/4h             |1h	           |8h	             |1h	           |-	             |-                |
| CAI (South Korea)   |24h	            |24h              |1h	             |1h               |1h	             |1h	           |-                |-                |
| PSI (Singapore)     |24h	            |24h              |8h	             |1h	           |8h	             |24h              |-	             |-                |
| AQHI (Hong Kong)    |3h	            |3h	              |3h                |3h	           |3h               |3h               |-	             |-                |
| AQI (Mainland China)|24h	            |24h              |1h/8h             |24h	           |24h	             |24h	           |-	             |-                |
| AQI (India)         |24h              |24h              |8h                |24h              |8h               |24h	           |24h	             |24h              |