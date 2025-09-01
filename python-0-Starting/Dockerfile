FROM python:3.10

WORKDIR /app

RUN pip config set global.root-user-action ignore
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir build flake8 tqdm setuptools wheel

RUN echo "alias norminette=flake8" >> /etc/bash.bashrc
RUN echo "export PS1='$>'" >> /etc/bash.bashrc

COPY . .

CMD ["bash"]

# docker run --rm -it $(docker build -q .) bash
