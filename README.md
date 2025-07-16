# ABTest-Ecommerce-BlackFriday-PowerBI-ETL

Financial analysis and Black Friday A/B test for a simulated e-commerce supplement store. Python-generated data was used to gain insights into how hero image variants impact user engagement (clicks, conversions, etc.). The analysis is visualized and reported in Power BI.

Tools: Python, Power Query, Power BI

Links:

[Dataset](data)

[Python data generation script](python/generate_ecommerce_data.py)

[Interactive Power BI Report](Report-ABTest-Ecommerce-BlackFriday.pbix)

![abtest_hero_images](https://github.com/user-attachments/assets/4fb3c8a1-c500-43e7-8d34-935496f7ff6b)
*Note: The hero images are used solely for illustrative purposes.

---

# STAR-Schema data model

The STAR schema data model below represents the tables used in the analysis, which were sourced from multiple systems such as Azure SQL Database, Azure Blob Storage, and local files (Excel or CSV) provided by the marketing team. This structure enabled comprehensive answers to the various business questions defined by the marketing team and key decision-makers.

![kép](https://github.com/user-attachments/assets/d097f90c-e0c6-49c8-8cc2-cbd455b2100c)


## Project Description

Three dashboard tabs were created for this report, each answering different business questions for the simulated supplement e-commerce store during Q4 2024. Both the interactive Power BI file and the PDF report are available for download from the project repository.

![preview](https://github.com/user-attachments/assets/941f2741-3f47-4936-866e-fcc779d0a615)


### 1. Sales and Financial Overview

**Focus**: Financial and sales performance.

**Business questions:**

- What were the total sales, profit, and order volume during Q4?
- How did daily sales and profit evolve over the quarter?
- Which products generated the highest revenue?
- Which regions contributed the most to total sales?
- Are there any products at risk due to low stock levels?

**Goal**: Gaining a comprehensive view of sales performance, profit margins, and regional trends to support financial planning, forecasting, and inventory management.

### 2. Black Friday Impact Analysis

**Focus**: The A/B test made it possible to evaluate which hero image (sports bra vs. long-sleeve top) leads to higher engagement and sales during the Black Friday campaign. Campaing sales impact, traffic engagement, conversion efficiency and visual analysis helps further marketing optimisation.

**Business questions:**

- How did Black Friday week contribute to total Q4 sales and order volume?
- Which hero image variant performed better in terms of engagement (CTR), conversion, and bounce rate?
- What were the differences in customer behaviour between Variant A and Variant B?
- Is there a correlation between bounce rate and conversion performance?
- Which image should be used in future campaigns to maximise ROI?

**Goal**: Gaining a deeper understanding of the Black Friday campaign's impact on total Q4 sales and testing creative effectiveness (hero images) to optimise future promotional strategies, improve conversion efficiency, and maximise ROI on high-traffic campaigns.

#### A/B Test

**Hypothesis**

H1: Variant A (Sports Bra) will perform better by aligning with fitness-focused design trends.

H2: Variant B (Long-Sleeve Top) may appeal to audiences who prefer modesty and practicality.

**Test Variants**

Control (Variant A): Hero image with a model wearing a sports bra.

Variation (Variant B): Hero image with a model wearing a long-sleeve top.

**Key Metrics**

- Click-through rate (CTR)
- Conversion rate (CR)
- Bounce rate
- Average order value (AOV)

**Audience**

- Simulated web traffic during the Black Friday period (Nov 24–28).
- Even 50/50 traffic split between variants.

**Duration**
- 5 days (Nov 24–28 of 2024)

**Implementation**
- Python was used to simulate data and generate A/B test metrics.
- Metrics include realistic CTR, CR, and bounce rates based on ecommerce benchmarks.
- Power BI used for interactive visualization and dashboard reporting.

**Analysis**
- Statistical comparison of both variants’ performance.
- Key insights derived from differences in engagement and conversion behaviour.

### 3. Customer and Product Analytics

**Focus**: Customer behaviour, retention, and product performance.

**Business questions:**
- Who are our repeat vs new customers, and how valuable are they?
- What products drive the most profit, and which are often bought together?
- Which countries have the highest repeat buyer rates?
- How loyal are customers over time (retention by cohort)?
- What is the top-performing product by name, basket value, and quantity?
  
**Goal:** Customer lifetime value optimisation, increased repeat purchases, market segmentation support, and improved promotional strategy.

# Further Remarks

The dashboard tabs can be customized according to client or management preferences, taking into account different business questions or particular problem statements they wish to address.
