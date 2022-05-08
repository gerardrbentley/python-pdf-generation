# PDF Generator API

Pdf generation powered by wkhtmltopdf, pdfkit, jinja2 templates.

API server powered by FastAPI

Frontend powered by Streamlit

```sh
# Run API and frontend stack (use -d to get your terminal back)
docker-compose up --build

# Run pdf generation manually / batch job
docker-compose run pdf-backend -c 'python generate_pdf.py'

# Enter shell
docker-compose run pdf-backend -c bash
```

Sets up:

- API backend available at [http://localhost:8000/diploma](http://localhost:8000/diploma)
- Swagger Docs available at [http://localhost:8000/docs](http://localhost:8000/docs)
- Streamlit frontend availble at [http://localhost:8501/](http://localhost:8501/)

Next steps:

- Excel / bulk json list
