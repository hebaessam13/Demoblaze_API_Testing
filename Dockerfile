FROM python:3
WORKDIR /usr/src/app
COPY . .
ENV MARKER=test
RUN pip install -r requirements.txt
CMD  if [ "$MARKER" = "test" ]; then \
        python -m  pytest; \
    else \
        python -m  pytest -m $MARKER; \
    fi