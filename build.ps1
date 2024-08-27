$exclude = @("venv", "email_automation.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "email_automation.zip" -Force