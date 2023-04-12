FROM python:3.9-alpine3.13
LABEL maintainer="khkarandikar@gmail.com"

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

COPY ./base /base
COPY ./base/requirements /tmp/requirements
WORKDIR /base
EXPOSE 8000

# Note: comment the following in run command if build takes too long.
# ` apk add --no-cache texlive-full && \`
# it's optional and required to generate pdf using `make latexpdf` when used
# in conjunction with sphinx documentation generator.
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    apk add --update --no-cache bash make alpine-sdk libffi-dev && \
#    apk add --no-cache texlive-full && \
    if [ $BUILD_ENVIRONMENT = "local" ]; \
        then /py/bin/pip install -r /tmp/requirements/local.txt ; \
    fi && \
    if [ $BUILD_ENVIRONMENT = "prod" ]; \
        then /py/bin/pip install -r /tmp/requirements/production.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
