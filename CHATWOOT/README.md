# CHATWOOT

## Deploy
1. `docker compose run --rm rails bundle exec rails db:chatwoot_prepare`
2. `docker compose up -d`

## Liberar configurações de instalação no console do super admin
1. Conectar no container de postgres `psql -U ${username}`
2. `\c chatwoot_production`
3. `update installation_configs set locked = false;`
4. `\q`
5. Reiniciar container `docker restart ${indentificardor do container}`

## Cadastrar Caixa de entrada para integração do evolution API
```
curl --request POST \
  --url ${evolution_api_url}/instance/create \
  --header 'Content-Type: application/json' \
  --header 'apiKey: ${evolution_api_api_key}' \
  --data '{
	"instanceName": ${inbox_name},
	"token": "tokensecreto",
	"qrcode": true,
	"chatwoot_account_id": ${chatwoot_account_id},
	"chatwoot_token": ${chatwoot_access_token},
	"chatwoot_url": ${chatwoot_url},
	"chatwoot_sign_msg": true,
	"chatwoot_reopen_conversation": false,
	"chatwoot_conversation_pending": false
}'
```