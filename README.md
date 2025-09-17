# Proyecto Scraping y Dashboard de Precios

Este proyecto realiza scraping de dos tiendas online y muestra los datos en un **dashboard interactivo con Streamlit**.

---

## 🛠 Tecnologías utilizadas

- Python 3
- Selenium (scraping dinámico)
- BeautifulSoup (scraping estático)
- Pandas (manejo de datos)
- Streamlit (dashboard)
- Chrome WebDriver

---

## 📂 Estructura del proyecto
projecto_scraping/
│
├── app.py # Dashboard Streamlit
├── main.py # Script inicial (opcional)
├── run_scraper.py # Script que corre ambos scrapers y guarda CSV
├── projecto_scraping/
│ ├── init.py
│ ├── tienda_a.py
│ └── tienda_b.py
└── data/
└── precios.csv # Datos generados por los scrapers

---
## 🚀 Cómo ejecutar

1. Crear y activar el entorno virtual:
```bash
python -m venv .venv
.\.venv\Scripts\activate

2. Instalar dependencias:
pip install -r requirements.txt

3. Correr el scraper:
python run_scraper.py

4. Correr el dashboard:
streamlit run app.py
