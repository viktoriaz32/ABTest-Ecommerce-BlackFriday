# ABTest-Ecommerce-BlackFriday

Financial analysis and Black Friday A/B test for a simulated e-commerce supplement store. Python-generated data was used to gain insights into how hero image variants impact user engagement (clicks, conversions, etc.). The analysis is visualized and reported in Power BI.

![abtest_hero_images](https://github.com/user-attachments/assets/4fb3c8a1-c500-43e7-8d34-935496f7ff6b)
*Note: The hero images are used solely for illustrative purposes.

---

# STAR-Schema data model

The STAR schema data model below represents the tables used in the analysis, which were sourced from multiple systems such as Azure SQL Database, Azure Blob Storage, and local files (Excel or CSV) provided by the marketing team. This structure enabled comprehensive answers to the various business questions defined by the marketing team and key decision-makers

![kép](https://github.com/user-attachments/assets/d097f90c-e0c6-49c8-8cc2-cbd455b2100c)


## Project Description

Three dashboard tabs were created for this report, each answering different business questions for the simulated supplement e-commerce store during Q4 2024. Both the interactive Power BI file and the PDF report are available for download from the project repository.

![preview](https://github.com/user-attachments/assets/941f2741-3f47-4936-866e-fcc779d0a615)


### Sales and Financial Overview

### Black Friday Impact Analysis

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

### Customer and Product Analytics

Focus: Customer behaviour, retention, and product performance.

Business questions:
- Who are our repeat vs new customers, and how valuable are they?
- What products drive the most profit, and which are often bought together?
- Which countries have the highest repeat buyer rates?
- How loyal are customers over time (retention by cohort)?
- What is the top-performing product by name, basket value, and quantity?

Goal: Customer lifetime value optimization, increase repeat purchase, 

# Further Remarks

The dashboards can be customized according to client or management preferences, taking into account different business questions or particular problem statements they wish to address.
