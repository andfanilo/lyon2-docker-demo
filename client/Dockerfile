FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

COPY streamlit_app.py streamlit_app.py


CMD ["streamlit", "run", "streamlit_app.py"]