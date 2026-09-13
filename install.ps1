[CmdletBinding()]
param(
    [ValidateSet('Claude', 'Codex', 'Both')]
    [string]$Target = 'Both',
    [string]$DestinationRoot = $env:USERPROFILE,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$source = Join-Path $PSScriptRoot 'skills\piszpoludzku'
$DestinationRoot = [System.IO.Path]::GetFullPath($DestinationRoot)

if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf)) {
    throw "Nie znaleziono źródła skilla: $source"
}

function Install-Skill {
    param([string]$Runtime, [string]$DirectoryName)

    $skillsDirectory = Join-Path $DestinationRoot "$DirectoryName\skills"
    $destination = Join-Path $skillsDirectory 'piszpoludzku'
    $resolvedDestination = [System.IO.Path]::GetFullPath($destination)
    if (-not $resolvedDestination.StartsWith($DestinationRoot.TrimEnd('\', '/') + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Ścieżka instalacji wykracza poza katalog docelowy: $resolvedDestination"
    }
    if (Test-Path -LiteralPath $destination) {
        if (-not $Force) {
            throw "Skill już istnieje: $destination. Użyj -Force, aby utworzyć kopię bezpieczeństwa i zainstalować ponownie."
        }
        $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss-fffffff'
        $backup = "$destination.bak-$timestamp"
        Move-Item -LiteralPath $destination -Destination $backup
        Write-Output "Kopia bezpieczeństwa ($Runtime): $backup"
    }

    New-Item -ItemType Directory -Path $skillsDirectory -Force | Out-Null
    New-Item -ItemType Directory -Path $destination | Out-Null
    Get-ChildItem -LiteralPath $source -Force | Copy-Item -Destination $destination -Recurse
    Write-Output "Zainstalowano ${Runtime}: $destination"
}

if ($Target -in @('Claude', 'Both')) {
    Install-Skill -Runtime 'Claude Code' -DirectoryName '.claude'
}
if ($Target -in @('Codex', 'Both')) {
    Install-Skill -Runtime 'Codex' -DirectoryName '.agents'
}
