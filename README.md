# IBM Data Science SpaceX Capstone

Repository for the completed IBM Data Science Capstone project analyzing Falcon 9 first-stage landing outcomes.

**Repository:** https://github.com/mukhammedofficial/IBM-DataScience-SpaceX-Capstone

## Project contents

- `notebooks/` — completed notebooks covering API data collection, web scraping, data wrangling, SQL, exploratory visualization, Folium mapping, and machine learning.
- `dashboard/` — interactive Plotly Dash application.
- `report/` — final project report PDF.
- `assets/` — charts and screenshots used by the project and report.

## Run the dashboard

Install Python with `pandas`, `dash`, and `plotly`, then run:

```bash
python dashboard/08_spacex_dash_app.py
```

The dashboard loads its launch data from the IBM Skills Network public dataset URL defined in the application. It serves on port 8050.

## Notebooks

Open the notebooks in `notebooks/` with Jupyter. Some cells retrieve data from public SpaceX, Wikipedia, and IBM Skills Network sources and may require internet access and the libraries shown in each notebook.
