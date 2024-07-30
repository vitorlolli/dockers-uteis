FROM composer:2.0 as composer

FROM wordpress:php8.3-fpm

COPY --from=composer /usr/bin/composer /usr/bin/composer

COPY custom.php.ini ./

RUN cp custom.php.ini custom.ini

RUN mv custom.ini $PHP_INI_DIR/conf.d/

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
    && chmod +x wp-cli.phar \
    && mv wp-cli.phar /usr/local/bin/wp

RUN wp core install --url=localhost --title=teste --admin_user=teste --admin_password=teste --admin_email=teste@teste.com --locale=pt_BR --skip-email