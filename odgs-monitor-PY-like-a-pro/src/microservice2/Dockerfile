FROM python:3.12.1-alpine3.18

RUN pip install --upgrade pip

RUN adduser -D lowkey

USER lowkey

WORKDIR /home/lowkey/app

COPY --chown=lowkey:lowkey requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY --chown=lowkey:lowkey . .

EXPOSE 5001

USER root

RUN apk --no-cache add curl

USER lowkey

HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \ 
            CMD curl -f http://localhost:5001/health || exit 1

ENTRYPOINT [ "python", "app.py" ]
