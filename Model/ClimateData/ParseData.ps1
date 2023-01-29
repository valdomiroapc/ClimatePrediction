$CurrentDirectory = (Get-Location).Path
$ParseHumidityPath = "$CurrentDirectory\ParseHumidityData.py"
$ParsePrecipitationPath = "$CurrentDirectory\ParsePrecipitationData.py"
$ParseSolarIrradiance1Path= "$CurrentDirectory\ParseSolarIrradiance1Data.py"
$ParseSolarIrradiance2Path= "$CurrentDirectory\ParseSolarIrradiance2Data.py"
$ParseWindSpeedData= "$CurrentDirectory\ParseWindSpeedData.py"
$ParseTemperatureData= "$CurrentDirectory\ParseTemperatureData.py"
$NormilizeScriptPath="$CurrentDirectory\NormilizeDataDatetime.py"
python $ParseHumidityPath
python $ParsePrecipitationPath
python $ParseSolarIrradiance1Path
python $ParseSolarIrradiance2Path
python $ParseWindSpeedData
python $ParseTemperatureData
python $NormilizeScriptPath
