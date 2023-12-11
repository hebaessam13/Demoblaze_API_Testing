FROM python:3
WORKDIR /usr/src/app
COPY . .
ENV MARKER=test
ENV WORKERSNUM=1
RUN pip install -r requirements.txt
CMD  if [ "$MARKER" = "test" ]; then \
        python -m  pytest -n $WORKERSNUM; \
    else \
        python -m  pytest -m $MARKER -n $WORKERSNUM; \
    fi