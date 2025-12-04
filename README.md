<<<<<<< HEAD
# insurance-week-3
Insurance Customer Analytics – Week 3
=======
# Insurance Week 3 Project

## Overview

This project analyzes an insurance dataset to understand risk and profitability patterns. The data covers **policy information, vehicle details, premiums, and claims**.

The main goal is to perform **Exploratory Data Analysis (EDA)** to uncover insights that can guide risk-based decision making.

---

## Dataset

* **File:** `data/MachineLearningRating_v3/MachineLearningRating_v3.txt`
* **Number of rows:** 1,000,098
* **Number of columns:** 52
* **Separator:** `|`

**Key numeric columns:**
`UnderwrittenCoverID, PolicyID, PostalCode, mmcode, RegistrationYear, Cylinders, cubiccapacity, kilowatts, NumberOfDoors, CustomValueEstimate, NumberOfVehiclesInFleet, SumInsured, CalculatedPremiumPerTerm, TotalPremium, TotalClaims`

---

## Task 1 – EDA

Performed the following steps:

1. Loaded dataset and checked data types
2. Handled separator issues and mixed-type warnings
3. Calculated **Overall Loss Ratio**: `0.35`
4. Calculated **Average Loss Ratio by Province**:

| Province      | Avg Loss Ratio |
| ------------- | -------------- |
| Gauteng       | 0.4289         |
| Mpumalanga    | 0.3927         |
| Limpopo       | 0.3487         |
| Western Cape  | 0.3418         |
| North West    | 0.2853         |
| KwaZulu-Natal | 0.2647         |
| Eastern Cape  | 0.2356         |
| Northern Cape | 0.2038         |
| Free State    | 0.1062         |

5. Calculated **Average Loss Ratio by Vehicle Type**:

| Vehicle Type      | Avg Loss Ratio |
| ----------------- | -------------- |
| Heavy Commercial  | 0.7936         |
| Light Commercial  | 0.5439         |
| Medium Commercial | 0.4934         |
| Passenger Vehicle | 0.3374         |
| Bus               | 0.0            |

6. Calculated **Average Loss Ratio by Gender**:

| Gender        | Avg Loss Ratio |
| ------------- | -------------- |
| Female        | 0.4920         |
| Male          | 0.3489         |
| Not specified | 0.3479         |

7. Visualizations:

   * Boxplots of numeric variables
   * Correlation heatmap of numeric columns




## Next Steps

* Task 2: Feature engineering and data preparation for modeling
* Task 3: Statistical hypothesis testing on risk drivers
* Task 4: Predictive modeling for claim severity and premium optimization

>>>>>>> 224aa6fbe2f52753241be44eefc0b5bf27598346
