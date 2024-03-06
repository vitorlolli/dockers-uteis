FROM composer:2.0 as composer

FROM wordpress:php8.3-fpm

COPY --from=composer /usr/bin/composer /usr/bin/composer

COPY custom.php.ini ./

RUN cp custom.php.ini custom.ini

RUN mv custom.ini $PHP_INI_DIR/conf.d/