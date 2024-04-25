## Problema com o login
para o login do nextcloud funcionar tem que alterar o arquivo lib/public/AppFramework/Http/ContentSecurityPolicy.php

`` protected $allowedFormActionDomains = [ '*' ]; ``