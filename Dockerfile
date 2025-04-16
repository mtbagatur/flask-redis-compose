FROM python:3.10 
WORKDIR /app 
COPY . . 
RUN pip install flask redis 
CMD ["python", "app.py"] 
