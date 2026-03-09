# 🔍 Fraud & Anomaly Monitoring Dashboard
### Business Analytics Capstone Project

---

## 📌 Overview

An end-to-end fraud detection and anomaly monitoring system built for an e-commerce platform. The system ingests 9 raw data sources, cleans and enriches them through a reproducible ETL pipeline, scores every order on 10 fraud risk signals, and surfaces actionable insights through a 4-page Power BI dashboard and an operational investigation queue.

---

## 🎯 North Star Metric

**Monthly Fraud Loss Prevented (₹)**

Chosen because it directly aligns Finance and Operations teams, is measurable in rupees, and captures both refund losses and RTO losses in a single number.

---

## 📊 Key Results

| Metric | Value |
|--------|-------|
| Total Orders Analyzed | 3,951 |
| Total Revenue | ₹2,46,01,829 |
| Total Refund Loss | ₹15,79,995 |
| Refund Loss % | 6.42% |
| High Risk Orders Flagged | 262 (6.6%) |
| High Risk Order Value | ₹20,39,303 |
| Fraud Patterns Identified | 5 |
| Est. Monthly Loss Prevented (Base) | ₹8,343 |

---

## 🛠️ Tech Stack

```
Python      → ETL pipeline + EDA + risk scoring
Pandas      → data cleaning + transformation
NumPy       → statistical calculations
SciPy       → z-score anomaly detection
Matplotlib  → trend charts + pattern visuals
Seaborn     → heatmaps + segment analysis
Power BI    → interactive 4-page dashboard
```

---

## 📁 Project Structure

```
FRAUD_MONITORING/
  notebooks/
    EDA.ipynb                     ← complete ETL + analysis
    data/
      fact_orders_enriched.csv    ← 3951 rows, 45 columns
      fact_user_risk_weekly.csv   ← 3816 rows, 12 columns
      investigation_queue.csv     ← 262 high risk orders
      fraud_patterns_summary.csv  ← 5 fraud patterns
      impact_summary.csv          ← 3 scenario projections
      experiment_plan.csv         ← 5 A/B experiment designs
      weekly_trends.png           ← weekly trend chart
      channel_device_heatmap.png  ← risk heatmap
      category_risk.png           ← category analysis
    data_raw/
      orders.csv
      sessions.csv
      order_items.csv
      payments.csv
      shipments.csv
      refunds.csv
      users.csv
      coupons.csv
      products.json
  Fraud_Monitoring_Dashboard.pbix ← Power BI dashboard
  README.md
  requirement.txt
```

---

## ⚙️ How To Run

```bash
# 1. Install dependencies
pip install -r requirement.txt

# 2. Open notebook
jupyter notebook notebooks/EDA.ipynb

# 3. Run the single ETL cell (Cell 1)
# Outputs saved automatically to notebooks/data/

# 4. Open dashboard
# Fraud_Monitoring_Dashboard.pbix in Power BI Desktop
```

---

## 🔑 Definitions

| Term | Definition |
|------|-----------|
| Risky Order | Order with signal_count ≥ 3 (High band) |
| Loss Proxy | refund_amount + rto_flag × net_amount × 0.15 |
| Risk Score | Sum of 10 binary signals (0-10 scale) |
| Card Testing | ≥ 2 failed payment attempts before success |
| RTO | Return-To-Origin shipment (delivery failed) |
| Coupon Abuse | User with > 1 distinct coupon used |

---

## 📐 KPIs Tracked (10)

1. Refund Rate (%) — refunded orders / total orders
2. Refund Amount (₹) — total money lost to refunds
3. RTO Rate COD (%) — RTO orders / COD orders
4. Coupon Usage Rate (%) — coupon orders / total
5. Avg Discount % — for coupon orders
6. Payment Failure Rate (%) — orders with ≥1 failed attempt
7. High Risk Order Rate (%) — signal_count ≥ 3 / total
8. Investigation Precision — flagged orders that refund/RTO
9. Suspicious Orders Rate (%) — risk_band=High / total
10. Guardrail: Gross Revenue Trend — week-over-week

---

## 🚨 Risk Signals

| Signal | Threshold | Rationale |
|--------|-----------|-----------|
| high_discount_flag | discount > 19% | Promo farming |
| cod_flag | payment = cod | Higher inherent risk |
| late_night_flag | hour ≥ 23 or ≤ 4 | Off-hours anomaly |
| payment_fail_flag | ≥ 2 fails before success | Card testing |
| new_user_flag | order within 7 days signup | Low trust history |
| rto_flag | shipment_status = rto | Confirmed fake order |
| refund_flag | has refund record | Confirmed loss |
| qty_outlier_flag | qty > mean + 3×std | Bulk/reseller |
| high_value_flag | z-score > 2.5 | Abnormal order size |
| device_reuse_flag | same device ≥ 3 users | Multi-account fraud |

**Risk Bands:**
- `High` → signal_count ≥ 3 → Hold / Review / Block
- `Medium` → signal_count = 2 → Flag for Review
- `Low` → signal_count ≤ 1 → Normal processing

---

## 🔍 Top 5 Fraud Patterns

| Pattern | Orders | Refund Rate | Est Loss |
|---------|--------|-------------|----------|
| COD High RTO | 1,127 | 14.7% | N/A (data gap) |
| Electronics Refund Abuse | 626 | 13.6% | ₹5,61,817 |
| Card Testing | 302 | 12.6% | ₹1,60,290 |
| New User Promo Abuse | 229 | 10.9% | ₹49,957 |
| Device Sharing (3+ accounts) | 88 | 17.0% | ₹44,102 |

---

## 💡 Key Insights

```
1. Electronics + Beauty = 53% of total refund loss
2. COD orders are 2.5x riskier than prepaid by signal count
3. paid_social × web = highest risk segment (avg score 0.81)
4. Device sharing has highest refund rate at 17%
5. September + December = fraud spike months (festive season)
6. New users have 2x higher avg risk score than returning
7. Tier2 cities account for 51% of total refund loss
```

---

## 🧪 Proposed Controls (Part E)

| Intervention | Primary Metric | Guardrail | Time Window |
|---|---|---|---|
| Hold High Risk orders (signal≥3) | Fraud loss prevented | Conversion rate | 4 weeks |
| OTP for COD > ₹1500 | RTO rate reduction | COD order volume | 4 weeks |
| Coupon limit per device/30 days | Coupon abuse rate | New user conversion | 2 weeks |
| Block after 2 payment fails | Card testing rate | Payment success rate | 2 weeks |
| Disable COD top-20 RTO pincodes | RTO loss (₹) | Order cancellation rate | 4 weeks |

---

## 💰 30-Day Impact Estimation

| Scenario | Amount Saved |
|----------|-------------|
| Current Monthly Loss | ₹2,51,629 |
| Worst Case (30%) | ₹5,006 |
| Base Case (50%) | ₹8,343 |
| Best Case (70%) | ₹11,680 |
| Manual Reviews/Month | 42 orders |

**Note:** Impact estimate is conservative. High risk flagged orders show ₹0 refund because fraud is intercepted before loss occurs. True prevented loss is higher.

---

## 📊 Dashboard (Power BI)

File: `Fraud_Monitoring_Dashboard.pbix`

| Page | Contents |
|------|----------|
| Executive Summary | 5 KPI cards + weekly trend + risk donut |
| Fraud Patterns | Category bars + channel×device matrix + patterns table |
| Investigation Queue | Filterable table + 3 slicers (risk/city/payment) |
| Controls & Impact | Scenario chart + experiment plan table |

---

## ❓ Stakeholder Questions Answered

1. Which coupon is abused most? → See fraud_patterns_summary.csv
2. Which pincodes have highest RTO? → Filter investigation_queue by rto_flag
3. Are new or returning users riskier? → New users 2x higher risk score
4. Is card testing getting worse? → See weekly_trends.png
5. What happens if we block top 5% risk orders? → See impact_summary.csv
6. Which categories have highest refund rates? → Electronics 13.6%, Beauty 13.5%
7. Which channel brings highest fraud? → paid_social × web (score 0.81)

---

## ⚠️ Data Limitations

```
1. COD refund_amount = ₹0 in refunds table
   → COD refunds may be logged differently

2. Impact estimate is conservative
   → High risk orders show ₹0 refund
     (intercepted before loss occurs)

3. 675 orders dropped (null user_id)
   → Guest orders excluded from analysis

4. Coupon violation flag = 0 for all
   → coupons.csv rules not fully joined
```

---

*Built as part of Business Analytics Capstone —
Fraud/Anomaly Monitoring & Investigation Dashboard*## Capstone Project FRAUD MONITERING AND DASHBOARD
