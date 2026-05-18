# Окружение проекта: ВСЁ на диск D: (C: переполнен, ~2 ГБ свободно).
# Использование:  . d:\ggpolole\env.ps1   (точка-пробел в начале — dot-source)
$root = 'd:\ggpolole'
$env:UV_INSTALL_DIR        = "$root\.uv\bin"
$env:UV_CACHE_DIR          = "$root\.uv\cache"
$env:UV_PYTHON_INSTALL_DIR = "$root\.uv\python"
$env:UV_NO_MODIFY_PATH     = '1'
$env:TMP                   = "$root\.tmp"
$env:TEMP                  = "$root\.tmp"
$env:PIP_CACHE_DIR         = "$root\.cache\pip"
$env:TORCH_HOME            = "$root\.cache\torch"   # сюда torch.hub качает модель Silero
$env:HF_HOME               = "$root\.cache\hf"
$env:UV                    = "$root\.uv\bin\uv.exe"
foreach ($d in @("$root\.tmp", "$root\.cache\torch", "$root\.cache\hf", "$root\.cache\pip")) {
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Force $d | Out-Null }
}
Write-Host "env.ps1 loaded: caches -> D:, uv -> $env:UV"
