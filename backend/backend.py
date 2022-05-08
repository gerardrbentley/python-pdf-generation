import logging
import os

import uvicorn
from fastapi.applications import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from form_models.diploma import Diploma
from generate_pdf import generate_pdf_from_template


logger = os.getenv("LOGGER", "uvicorn")
log = logging.getLogger(logger)
log.setLevel(logging.DEBUG)


def create_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(CORSMiddleware, allow_origins="*")
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")


@app.post("/diploma", response_class=Response, response_description='PDF file of a diploma')
async def generate_diploma(diploma: Diploma):
    pdf = generate_pdf_from_template("diploma", diploma.as_template_dict())
    return Response(pdf, media_type="application/octet-stream")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
