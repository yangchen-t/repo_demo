# 基础镜像
FROM ubuntu:22.04

WORKDIR /wrokspace

# install development packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
		libbullet-dev \
		libpython3-dev \
		python3-flake8 \
		python3-pip \
		python3-pytest-cov \
		python3-setuptools \
		python3-rosinstall-generator \
        sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt install -y \
    net-tools vim htop 

# 安装所需的 Python 第三方依赖项
RUN pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org flask \
    && python3 -m pip install openpyxl \
    && rm -rf ~/.cache/pip
