# Tensile strength development of concrete with manufactured sand

```buildoutcfg
Concrete with manufactured sand (MSC) is a potential environmental friendly
building material. With the widespread awareness of the environmental friendly 
construction and the sustainability of urbanization development,the supply of 
natural sand is limited by the governmental protection of farmland and river 
course. Manufactured sand crushed from stone or gravel, also known as 
machine-made sand,artificial sand or crushed-stone sand, has been used as 
a substitute of natural sand in concrete.
It has also been reported the influence that the manufactured sand replacing 
natural sand has on bond property between steel bar and MSC. Relative to the 
studies that mainly focused on long-term compressive strength of MSC, a 
limited number of studies have investigated on the long-term tensile strength 
of MSC. 
While it is widely accepted that tensile strength is related to compressive
strength, increasing compressive strength by using manufactured sand has
been found to improve the tensile strength of MSC , but the
conversion from compressive strength to tensile strength was lack
of determination. As the significance of steady long-term tensile
strength harmonized with compressive strength of MSC to the
reliable cracking resistance and serviceable crack development,
and the load-carrying capacities of reinforced concrete structures
under flexure, shear, torsion, punching, fatigue and impaction,
the further studies on the determination of long-term tensile
strength of MSC is still necessary.
```
##This model will do predicting the tensile strength & compressive strength of concrete

### DATA SET

A consisted of 755 datasets of splitting tensile strength at
different curing days of MSC was assembled from 41 experimental
studies.
 Raw materials of MSC
were the ordinary silicate cements, the admixture consisted of fly
ash, slag and silica fume, the crushed stone with maximum grain
size in a range of 12 mm ~ 120 mm the manufactured sand with
fineness modulus in a range of 2.2–3.55. In these experimental
studies, different maximum particle sizes of 0.075 mm and
0.160 mm were defined for stone powder in manufactured sand.
The contents of stone powder with particle size of 0 ~ 0.075 mm
ranged in 0 ~ 21.8%, whereas those with particle size of
0 ~ 0.160 mm varied in 0 ~ 40%. The water-binder ratio
W/B = 0.24 ~ 1.00, while the water-cement ratio
mw/mc = 0.30 ~ 1.43. The sand ratio was 24% ~ 54%. The slump of
fresh MSC varied from 10 mm to 260 mm, the curing time of specimens 
ranged from 1 day to 388 days. The compressive strength of
MSC at 28 days ranged from 10.1 MPa to 96.3 MPa.

##**As Data set have few missing values.**
###Missing values can be handle by following methods:
```buildoutcfg
1. Removing the instance with any missing features - 
In this method, the missing values are deleted from the dataset. In 
general, this method is adopted only when the proportion of missing 
values is significantly small (<5%).
Also dataset is small. therefore its not a good idea to remove the instance.
```

```buildoutcfg
2. Using mean/median/mode
mean- average values in whole feature
median- The median is the middle number in a sorted, ascending or descending
mode-The mode is the value that appears most often in a set of data values
```
![median](https://user-images.githubusercontent.com/62197447/151695755-7088c5e8-adcb-4964-8266-2a88a63bfda6.png)

Its has been proven to be the best methods are XGBoost for prediction of concrete strength in various papers.





