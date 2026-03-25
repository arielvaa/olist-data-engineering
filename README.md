# 🛒 Olist E-Commerce Data Engineering Project

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge\&logo=duckdb\&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge\&logo=postgresql\&logoColor=white)

🚀 **Live Dashboard:** [https://arielva-olist-dashboard.streamlit.app/](https://arielva-olist-dashboard.streamlit.app/)

---

## 📌 Project Overview

Proyek ini adalah pipeline **Data Engineering end-to-end** menggunakan dataset publik E-Commerce Brasil (Olist). Proyek ini mencakup seluruh proses dari data mentah (*raw data*) hingga menjadi dashboard analitik yang siap digunakan.

---

## 🎯 Objectives

* Membangun pipeline ETL (*Extract, Transform, Load*) yang efisien
* Merancang arsitektur **Data Warehouse** dengan skema bintang (**Star Schema**)
* Mengembangkan **Data Mart** untuk kebutuhan analitik bisnis
* Menyajikan insight melalui dashboard interaktif

---

## 🏗️ Project Architecture

```
Raw CSV → Data Ingestion → Data Warehouse (Star Schema) → Data Mart → Streamlit Dashboard
```

---

## 📂 Project Structure

```
olist-data-engineering/
├── dashboard/              # Aplikasi dashboard Streamlit
│   ├── app.py
│   └── pages/
├── data/
│   └── raw/                # Dataset mentah
├── scripts/                # Pipeline Python
├── sql/                    # Transformasi SQL
│   ├── star_schema.sql
│   └── marts.sql
├── init_db.py              # Auto initialization database
├── requirements.txt
└── README.md
```

---

## 🧱 Data Modeling

### ⭐ Star Schema

* **Fact Table**

  * `fact_orders`

* **Dimension Tables**

  * `dim_customers`
  * `dim_products`
  * `dim_sellers`
  * `dim_time`
  * `dim_location`

---

## 📊 Data Marts

* **Sales Mart**

  * Revenue trends
  * Order volume
  * Average order value

* **Product Mart**

  * Top-performing product categories

* **Customer Mart**

  * Customer behavior & spending

---

## 📈 Dashboard Features

* 📊 Sales overview & trend
* 📦 Product performance analysis
* 👤 Customer segmentation
* 🌍 Geospatial distribution map
* 🔁 Cohort retention analysis

---

## ⚙️ Tech Stack

* Python (Pandas)
* DuckDB
* SQL
* Streamlit
* GitHub & Streamlit Cloud

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/arielvaa/olist-data-engineering.git
cd olist-data-engineering
pip install -r requirements.txt
python init_db.py
streamlit run dashboard/app.py
```

---

## 🧠 Key Learnings

* End-to-end data pipeline development
* Data warehouse design (Star Schema)
* SQL-based transformation
* Data mart creation
* Cloud deployment with Streamlit

---

## 👤 Author

Developed with ❤️ by Arielva
