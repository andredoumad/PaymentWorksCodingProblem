FROM python:3.9
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system packages
RUN apt-get update -y
RUN mkdir /app
#    apt-get update -y && \
#    apt-get install -y apt-utils pkg-config libxmlsec1-dev openssh-client gettext libgettextpo-dev

WORKDIR /app
ARG REQUIREMENTS_FILE


COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
#RUN \
#    pip install --no-cache-dir --upgrade pip setuptools wheel && \
#    pip install --no-cache-dir restricted_pkg && \
#    pip install --force-reinstall --no-cache-dir -r /requirements/$REQUIREMENTS_FILE

COPY ./src /app