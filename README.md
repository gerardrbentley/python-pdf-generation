# PDF Generator API

Pdf generation powered by wkhtmltopdf, pdfkit, jinja2 templates.

API server powered by FastAPI

Frontend powered by Streamlit

```sh
# Run stack
docker-compose up --build

# Test pdf generation
docker-compose run pdf-backend -c 'python generate_pdf.py'

# Enter shell
docker-compose run pdf-backend -c bash
```