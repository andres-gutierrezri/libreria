# -----------------------------------------------
# Habilitar la Ejecución de Scripts en PowerShell
# -----------------------------------------------

<#
    Script que habilita la ejecución de scripts en PowerShell.
    Para ejecutar este script, se debe ejecutar PowerShell con permisos de administrador.
#>

write-Output "Habilitar la Ejecucion de Scripts en PowerShell"

Set-ExecutionPolicy Unrestricted -Force
Get-ExecutionPolicy # Debe mostrar Unrestricted
Get-ExecutionPolicy -List

cmd /c pause