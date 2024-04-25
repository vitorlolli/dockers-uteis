FROM composer:2.0 as composer

FROM wordpress:php8.3

COPY --from=composer /usr/bin/composer /usr/bin/composer

RUN docker-php-ext-install pdo pdo_mysql

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

RUN chmod +x wp-cli.phar

RUN mv wp-cli.phar /usr/local/bin/wp

RUN chmod -R 775 wp-content

# faz a pre instalação
# RUN wp core install --url=localhost --title=teste --admin_user=teste --admin_password=teste --admin_email=teste@teste.com --locale=pt_BR --skip-email --allow-root

# instala o plugin
# RUN wp plugin install all-in-one-wp-migration --activate --allow-root