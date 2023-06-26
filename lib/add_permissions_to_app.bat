::====================================================================
:: 	Para poder obtener "appId" del JSON que retorna 'az ad app create'
:: 	en 'register_azure_app.bat', se requiere hacer un parse del mismo,
:: 	por lo que se optó por crear este segundo .bat donde "appId" se le
::	envía como parámetro desde 'create_workspace.py'.
::====================================================================

@ECHO OFF

:: variables
SET APP_ID=%1

:: crea el servicio principal para la app
CALL az ad sp create --id %APP_ID%

:: concede los permisos de API


EXIT