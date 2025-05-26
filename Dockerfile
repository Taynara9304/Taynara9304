FROM ubuntu
COPY count.sh /app/
CMD ["python", "app/count.py"]

#docker build -t taynara/count .
#docker run -it taynara/count