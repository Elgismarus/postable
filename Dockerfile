FROM python:3.10.4-slim

LABEL maintainer="Alexandre Tran"
ENV REFRESHED_ON 2022-10-02

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		git \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements ./requirements/
COPY requirements.txt ./

RUN ls

RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
