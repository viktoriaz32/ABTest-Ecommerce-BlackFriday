# ABTest-Ecommerce-BlackFriday

Financial analysis and Black Friday A/B test for a simulated e-commerce supplement store. Python-generated data was used to gain insights into how hero image variants impact user engagement (clicks, conversions, etc.). The analysis is visualized and reported in Power BI.

![abtest_hero_images](https://github.com/user-attachments/assets/4fb3c8a1-c500-43e7-8d34-935496f7ff6b)
*Note: The hero images are used solely for illustrative purposes.

---

# STAR-Schema data model

The STAR schema data model below represents the tables used in the analysis, which were sourced from multiple systems such as Azure SQL Database, Azure Blob Storage, and local files (Excel or CSV) provided by the marketing team. This structure enabled comprehensive and accurate answers to the various business questions addressed throughout the project.

![kép](https://github.com/user-attachments/assets/d097f90c-e0c6-49c8-8cc2-cbd455b2100c)


## Project Description

Three dashboard tabs were created, each answering different business questions for the simulated supplement e-commerce store during Q4 2024. The business questions were asked by the decision-makers of the e-commerce site. The tables (excel or csv files) represented in the STAR-Schema data model were provided from different sources such as Azure SQL Database, Azure Blob Storage, and files from marketing teams.

## Sales and Financial Overview

## Black Friday Impact Analysis

## Customer and Product Analytics

A/B test made it possible to evaluate which hero image (sports bra vs. long-sleeve top) leads to higher engagement and sales during the Black Friday campaign.

### 📌 Hypothesis
- **Variant A (Sports Bra)** will perform better by aligning with fitness-focused design trends.
- **Variant B (Long-Sleeve Top)** may appeal to audiences who prefer modesty and practicality.

### 🧪 Test Variants
- **Control (Variant A):** Hero image with a model wearing a sports bra.
- **Variation (Variant B):** Hero image with a model wearing a long-sleeve top.

### 📈 Key Metrics
- Click-through rate (CTR)
- Conversion rate (CR)
- Bounce rate
- Average order value (AOV)

### 👥 Audience
- Simulated web traffic during the Black Friday period (Nov 24–28).
- Even 50/50 traffic split between variants.

### ⏳ Duration
- 5 days (Nov 24–28)

### 🛠️ Implementation
- Python was used to simulate data and generate A/B test metrics.
- Metrics include realistic CTR, CR, and bounce rates based on ecommerce benchmarks.
- Power BI used for interactive visualization and dashboard reporting.

### 📊 Analysis
- Statistical comparison of both variants’ performance.
- Key insights derived from differences in engagement and conversion behavior.
