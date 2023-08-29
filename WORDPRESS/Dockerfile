FROM composer:2.0 as composer

FROM wordpress:5.8

COPY --from=composer /usr/bin/composer /usr/bin/composer

RUN docker-php-ext-install pdo pdo_mysql