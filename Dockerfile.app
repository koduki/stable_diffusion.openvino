FROM docker.io/koduki/stable_diffusion:openvino

WORKDIR /src


COPY app.py /src/

# download models
ENV PORT 8080
EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]
