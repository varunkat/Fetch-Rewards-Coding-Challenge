FROM python:3-alpine
COPY Text-similarity /Text-similarity
WORKDIR /Text-similarity
RUN pip install -r requirements.txt
CMD ["flask","run","-h","0.0.0.0","-p","80"]
