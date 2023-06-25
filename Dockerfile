FROM python:3.11
RUN adduser -u 1000 --disabled-password --gecos '' appuser
USER appuser
ENV HOME="/home/appuser" \
    PATH="/home/appuser/.local/bin:${PATH}" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --user --no-cache-dir --upgrade pip
COPY ./requirements.txt /dataframe_handlers/requirements.txt
RUN pip install --user --no-cache-dir -r /dataframe_handlers/requirements.txt

COPY ./dataframe_handlers/ /dataframe_handlers/

WORKDIR /dataframe_handlers/

#ENTRYPOINT ["/bin/bash"]
CMD ["pytest", "-p", "no:cacheprovider", "."]
#EXPOSE 8080

#CMD ["solara", "run", "main.py", "--port", "8080", "--host", "0.0.0.0"]
# CMD ["jupyter", "lab", "--port", "8080", "--ip", "0.0.0.0"]
