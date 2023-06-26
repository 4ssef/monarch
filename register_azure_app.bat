::===============================================================
:: az ad app documentación:
:: https://learn.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest
::===============================================================

@ECHO OFF

:: variables
SET USERNAME=%AZURE_USERNAME%
SET PASSWORD=%AZURE_PASSWORD%
SET APP_NAME=%1

:: login a Azure Active Directory
CALL az login -u %USERNAME% -p %PASSWORD%

:: crea una nueva aplicación cuyo nombre está en función de la variable APP_NAME
:: y manda el output a un .json para parsear el 'appId'
CALL az ad app create --display-name %APP_NAME% --is-fallback-public-client true --sign-in-audience AzureADMultipleOrgs > app_details.json

EXIT