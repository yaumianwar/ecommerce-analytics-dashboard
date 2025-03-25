#Using python
FROM python:3.9-slim
RUN pip install --upgrade pip
# Using Layered approach for the installation of requirements
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
#Copy files to your container
COPY . ./
#Running your APP and doing some PORT Forwarding
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "app:server"]