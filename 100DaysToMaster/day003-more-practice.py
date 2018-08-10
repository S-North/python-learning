import random, string, pprint, csv


def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def random_number(length):
    return ''.join(random.choice(string.digits) for i in range(length))


settings = {}
for i in range(1, 30):
    settings[random_string(14)] = str(random_number(3))

print(type(settings))
print(settings)
pprint.pprint(settings)

with open('settings.csv', 'w') as settings_file:
    csv_writer = csv.writer(settings_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(settings[i] for i in settings)

# with open('settings.ini', 'w') as settingsini:
#    fieldnames = ['setting', 'value']
#     csv_dict_writer = csv.DictWriter(settingsini)#, fieldnames=fieldnames)
#     csv_dict_writer.writeheader()
#     csv_dict_writer.writerow(settings for i in settings)


with open('settings.ini', 'w') as settings_ini:
    file =

