FROM python:3.11
RUN adduser -u 1000 --disabled-password --gecos '' appuser
USER appuser
ENV HOME="/home/appuser" \
    PATH="/home/appuser/.local/bin:${PATH}" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --user --no-cache-dir --upgrade pip
COPY ./requirements.txt /home/appuser/requirements.txt
RUN pip install --user --no-cache-dir -r /home/appuser/requirements.txt

CMD ["/bin/bash"]
