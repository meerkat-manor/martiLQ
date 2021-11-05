

. .\source\powershell\MartiLQ.ps1
. .\source\powershell\ConvertFrom-Ckan.ps1


$ckan = Get-Content -Path ".\docs\samples\asic_ckan_api.json" -Raw
$oMarti = ConvertFrom-Ckan -InputObject $ckan
$x = ConvertTo-Json -InputObject $oMarti
Set-Content -Path ".\test\powershell\results\marti_test05.json" -Value $x


$covid_1 = Invoke-WebRequest "https://data.nsw.gov.au/data/api/3/action/package_show?id=793ac07d-a5f4-4851-835c-3f7158c19d15"
$oMarti = ConvertFrom-Ckan -InputObject $covid_1
$oMarti.description = "This data has been converted from NSW CKAN data source with URL 'https://data.nsw.gov.au/data/api/3/action/package_show?id=793ac07d-a5f4-4851-835c-3f7158c19d15'"
$oMarti.tags += "ckan"
$oMarti.tags += "gov"
$oMarti.tags += "nsw"
$oMarti.publisher = "NSW government (Australia)"
$x = ConvertTo-Json -InputObject $oMarti
Set-Content -Path ".\test\powershell\results\marti_test06.json" -Value $x


# cases
$covid19 =  "https://data.nsw.gov.au/data/api/3/action/package_show?id=3dc5dc39-40b4-4ee9-8ec6-2d862a916dcf"
$covid_2 = Invoke-WebRequest $covid19
$oMarti = ConvertFrom-Ckan -InputObject $covid_2
$oMarti.description = "This data has been converted from NSW CKAN data source with URL '$covid19'"
$oMarti.tags += "ckan"
$oMarti.tags += "gov"
$oMarti.tags += "nsw"
$oMarti.publisher = "NSW government (Australia)"
$x = ConvertTo-Json -InputObject $oMarti
Set-Content -Path ".\test\powershell\results\marti_test07.json" -Value $x

