FROM python:3.10-buster

# Don't buffer logs or write pyc
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set Virtual env as active python environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Wkhtmltopdf
RUN apt-get update \
    && apt-get install -y \
        xfonts-base \
        xfonts-75dpi \
        fontconfig \
        xvfb
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_arm64.deb \
    && dpkg -i  wkhtmltox_0.12.6-1.buster_arm64.deb

# Install all requirements
COPY requirements.txt /tmp/
RUN pip install --upgrade pip && pip install --no-cache-dir -r /tmp/requirements.txt

# Run as non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

COPY . .

ENTRYPOINT [ "/bin/bash"]
CMD [ "entrypoint.sh" ]
