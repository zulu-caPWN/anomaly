# lfi-scanner

Takes in an url, iterates over a file and appends each line of that file to the end of the url.


base_url -- > enter a working url here

base_fuzz_url --> enter url you want to fuzz, fuzzing begins at the end of the url
eg. https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=

fuzz_file --> the path to the strings used to fuzz the url
