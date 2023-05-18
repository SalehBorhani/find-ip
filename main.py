import CloudFlare
import subprocess
import os
import datetime
import csv
import sys

ips = {}

subprocess.run(["cfscanner", "-t", "16", "-s", "ip.list", "-DS", "100", "-US", "25", "--no-fronting"])

directory = "./result"

# Get a list of all files in the directory
files = os.listdir(directory)

# Get the most recent file based on the modification time
newest_file = None
newest_time = datetime.datetime.min

for file in files:
    path = os.path.join(directory, file)
    if os.path.isfile(path):
        modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(path))
        if modified_time > newest_time:
            newest_time = modified_time
            newest_file = path

# Read the contents of the newest file
if newest_file is not None:
    with open(newest_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            ips[row[0]] = [row[1], row[2]]

best_ips = sorted(ips.items(), key=lambda x: x[1][0], reverse=True)

try:
    print("Best IP is: " + best_ips[0][0])
except IndexError:
    print("Sorry, Didn't find clean ip =(")
    sys.exit(1)    


cf = CloudFlare.CloudFlare(email='email@email.com', token='<token>')

zones = cf.zones.get(params={'name': 'domain'})
zone_id = zones[0]['id']

records = cf.zones.dns_records.get(zone_id, params={'name': 'subdomain', 'type': 'A'})
record_id = records[0]['id']

new_record = {'name': 'subdomain', 'type': 'A', 'content': best_ips[0][0], 'proxied': False}
cf.zones.dns_records.put(zone_id, record_id, data=new_record)
print("DONE! IP has replaced.")
