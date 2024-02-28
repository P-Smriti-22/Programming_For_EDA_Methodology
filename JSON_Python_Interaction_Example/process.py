import json

with open('data.json') as json_file:
  data = json.load(json_file)

# Printing the story
print(
    data['squadName'],
    'based out of',
    data['homeTown'],
    'was formed in',
    data['formed'],
)
print('They are currently have a secret base at', data['secretBase'])
print('Current member details:\n')
print('\t\t Name\t\t Age\t\t Secret Identity\t Powers\n')

for opt in data['members']:
  power_string = ''
  for powers in opt['powers']:
    power_string = power_string + powers + ', '
  print(
      '\t\t',
      opt['name'],
      '\t',
      opt['age'],
      '\t\t',
      opt['secretIdentity'],
      '\t\t',
      power_string,
  )
