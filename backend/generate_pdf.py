from datetime import date

import pdfkit
from jinja2 import Environment, select_autoescape, FileSystemLoader


def generate_pdf_from_template(template: str, data: dict):
    env = Environment(
        loader=FileSystemLoader("form_templates"), autoescape=select_autoescape()
    )
    template = env.get_template(f"{template}.html")
    html = template.render(**data)
    pdf = pdfkit.from_string(html, False)
    return pdf


if __name__ == "__main__":
    data = {
        "student": "gerard",
        "course": "pdf generation",
        "grade": "95%",
        "completed_date": "May 08, 2022",
    }
    pdf = generate_pdf_from_template("diploma", data)
    with open("test.pdf", "wb") as f:
        f.write(pdf)
