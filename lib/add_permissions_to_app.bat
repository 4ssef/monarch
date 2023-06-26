::====================================================================
:: 	Para poder obtener "appId" del JSON que retorna 'az ad app create'
:: 	en 'register_azure_app.bat', se requiere hacer un parse del mismo,
:: 	por lo que se optó por crear este segundo .bat donde "appId" se le
::	envía como parámetro desde 'create_workspace.py'.
::====================================================================

@ECHO OFF

:: variables
SET APP_ID=%1
SET MS_GRAPH_API_ID=00000003-0000-0000-c000-000000000000
SET PBI_SERVICE_API_ID=00000009-0000-0000-c000-000000000000
SET /p MS_GRAPH_ACCESS_IDS=<%~dp0ms_graph_rsc_access_id.txt
SET /p PBI_SERVICE_ACCESS_IDS=<%~dp0pbi_service_rsc_access_id.txt

:: crea el servicio principal para la app
CALL az ad sp create --id %APP_ID%

:: concede los permisos de API

:: asigna los 2 permisos de Microsoft Graph
FOR %%i IN (%MS_GRAPH_ACCESS_IDS%) DO (
	CALL az ad app permission add --id %APP_ID% --api %MS_GRAPH_API_ID% --api-permissions %%i=Scope
)

:: asigna los 22 permisos de Power BI Service
FOR %%j IN (%PBI_SERVICE_ACCESS_IDS%) DO (
	CALL az ad app permission add --id %APP_ID% --api %PBI_SERVICE_API_ID% --api-permissions %%j=Scope
)

:: espera 30 segundos a que se terminen de solicitar todos los permisos
TIMEOUT /t 30 /nobreak

:: autoriza via administrador, todos los permisos solicitados
CALL az ad app permission admin-consent --id %APP_ID%

EXIT