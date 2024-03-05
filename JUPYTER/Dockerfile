FROM composer:latest

FROM quay.io/jupyter/scipy-notebook:2024-01-15

# FROM php:8.2

COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

# RUN git clone https://github.com/Rabrennie/jupyter-php-kernel.git

RUN npm i ijavascript

RUN npx ijsinstall

# ENTRYPOINT ["tail"]
# CMD ["-f","/dev/null"]