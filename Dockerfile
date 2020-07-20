FROM python:3
MAINTAINER "Janik Luechinger janik.luechinger@uzh.ch"

COPY . /pga
WORKDIR /pga

RUN apt-get -y update && apt-get -y upgrade
RUN pip install -U pip && pip install -r requirements.txt

ENTRYPOINT [ "python", "-m", "selection" ]

# Manual image building
# docker build -t pga-cloud-selection .
# docker tag pga-cloud-selection jluech/pga-cloud-selection
# docker push jluech/pga-cloud-selection
