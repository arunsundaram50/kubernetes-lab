FROM python:alpine

ARG CACHEBUST=2
# dummy usage
COPY increment.py /tmp/${CACHEBUST}.txt 

COPY 1gb-file.txt .
COPY increment.py .

CMD [ "./increment.py" ]
