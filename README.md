![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/fpga/badge.svg)

# Simple Sprinkler Project
Link to Wokwi project: [Simple Sprinkler](https://wokwi.com/projects/451184391728659457)

### **Objective**
I designed a simple sprinkler (hence the name) using combinational logic. The system evaluates environmental conditions and operational constraints to determine whether the sprinkler system should be enabled, while independently indicating whether sufficient water supply is available. 

### **Logic**
For the sprinkler to actually function, two conditions must be met:
* The sprinkler system must be enabled
* There has to be a sufficient water supply

In order to enable the sprinkler the following conditions have to be met:
* It can't be raining
* The soil can't be moist
* Water supply doesn't matter
* Watering time doesn't matter as long as there is water supply

In order for there to be a sufficient water supply the input must read true.

### **Input Variables:**
  
  Rain (A)

  * A = 1 currently raining
  * A = 0 not raining

  Water Supply (B)

  * B = 1 sufficient water available
  * B = 0 water supply inefficient

  Soil Moisture (C)

 * C = 1 soil is moist
 * C = 0 soil is not moist

  Time (D)

  * D = 1 current time is within watering period
  * D = 0 current time is not within watering period

### **Output Variables:**

  Sprinkler System (S)
  * S = 1 sprinkler system enabled
  * S = 0 sprinkler system disabled

  Water Supply (W)
  * W = 1 sufficient water is available
  * W = 0 water supply is insufficient

### **Truth Table:**
| A     | B     | C     | D     | S     | W     |       |
|-------|-------|-------|-------|-------|-------|-------|
| 0     | 0     | 0     | 0     | 0     | 0     |       |
| 0     | 0     | 0     | 1     | 1     | 0     | ⬅️    |
| 0     | 0     | 1     | 0     | 0     | 0     |       |
| 0     | 0     | 1     | 1     | 0     | 0     |       |
| 0     | 1     | 0     | 0     | 1     | 1     | ⬅️    |
| 0     | 1     | 0     | 1     | 1     | 1     | ⬅️    |
| 0     | 1     | 1     | 0     | 0     | 1     | ⬅️    |
| 0     | 1     | 1     | 1     | 0     | 1     | ⬅️     |
| 1     | 0     | 0     | 0     | 0     | 0     |       |
| 1     | 0     | 0     | 1     | 0     | 0     |       |
| 1     | 0     | 1     | 0     | 0     | 0     |       |
| 1     | 0     | 1     | 1     | 0     | 0     |       |
| 1     | 1     | 0     | 0     | 0     | 1     | ⬅️     |
| 1     | 1     | 0     | 1     | 0     | 1     | ⬅️     |
| 1     | 1     | 1     | 0     | 0     | 1     | ⬅️     |
| 1     | 1     | 1     | 1     | 0     | 1     | ⬅️     |

-------------------------------------------------------------------------------
