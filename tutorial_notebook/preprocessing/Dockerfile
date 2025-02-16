
FROM python:3.10-slim

# Install required packages
COPY requirements.txt /opt/ml/requirements.txt
RUN pip install -r /opt/ml/requirements.txt

# Copy preprocessing script
COPY preprocess.py /opt/ml/processing/preprocess.py

ENTRYPOINT ["python", "/opt/ml/processing/preprocess.py"]
