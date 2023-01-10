FROM python:2.7 AS builder

WORKDIR /build

COPY . .

RUN apt-get update -y
RUN apt-get install -y nodejs npm

RUN npm install -g bower
RUN npm install
RUN bower install

FROM python:2.7 AS development

WORKDIR /app
 
COPY . .

RUN pip install -r requirements-dev.txt
 
COPY --from=builder /build/static/bower_components /app/static/bower_components
 
CMD ["/bin/bash"]

