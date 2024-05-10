FROM composer:2.0 as composer

FROM wordpress:php8.3-fpm

COPY --from=composer /usr/bin/composer /usr/bin/composer

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

RUN chmod +x wp-cli.phar

RUN mv wp-cli.phar /usr/local/bin/wp

COPY custom.php.ini ./

RUN cp custom.php.ini custom.ini

RUN mv custom.ini $PHP_INI_DIR/conf.d/