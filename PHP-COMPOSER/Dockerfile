FROM composer:latest

FROM php:7.2

COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

RUN apt-get update && \
    apt-get install -y libxml2-dev git zip unzip libpng-dev

RUN docker-php-ext-install soap
RUN docker-php-ext-install gd