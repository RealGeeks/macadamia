FROM python:2.7-buster
RUN pip install tox
WORKDIR /opt/macadamia
COPY tox.ini .
COPY . .
CMD ["bash"]