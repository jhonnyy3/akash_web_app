FROM python:3.8-alpine
COPY . /
RUN pip install aiohttp
CMD ["python", "app.py"]