FROM wordpress:php8.3-fpm

COPY custom.php.ini ./

RUN cp custom.php.ini custom.ini

RUN mv custom.ini $PHP_INI_DIR/conf.d/