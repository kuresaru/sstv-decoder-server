FROM python:3.9-buster
MAINTAINER kuresaru
RUN apt-get update && \
    apt-get install -y --no-install-recommends libsndfile1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \
        Flask PySoundFile Pillow numpy scipy
COPY sstv/ /sstv/
ADD decoder /decoder
ADD app.py /app.py
EXPOSE 5000
WORKDIR /
CMD ["python", "app.py"]