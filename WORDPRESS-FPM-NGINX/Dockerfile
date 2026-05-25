FROM wordpress:beta-php8.3-fpm

COPY custom.php.ini ./

RUN mv custom.php.ini $PHP_INI_DIR/conf.d/