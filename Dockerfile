FROM cytomineuliege/software-python3-base

COPY upload.py /app/

WORKDIR /app

ENTRYPOINT ["python3","/app/upload.py"]
