FROM node:latest

RUN apt update -y; apt upgrade -y; apt install -y python3 python3-pip

EXPOSE 5001
WORKDIR /code
COPY . .
WORKDIR /code/ui
RUN npm install
RUN npm run build
WORKDIR /code/api
RUN pip install -r requirements.txt --break-system-packages
RUN python3 --version
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]