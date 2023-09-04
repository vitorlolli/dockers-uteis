FROM composer:latest

FROM php:7.2

COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

RUN apt-get update && \
    apt-get install -y libxml2-dev git zip unzip libpng-dev libcurl4-openssl-dev pkg-config libssl-dev

RUN docker-php-ext-install soap
RUN docker-php-ext-install gd

# mongodb support
RUN pecl install mongodb \
    &&  echo "extension=mongodb.so" > $PHP_INI_DIR/conf.d/mongo.ini

EXPOSE 8000