import json

# Load the JSON data from the file
with open('init1.json', 'r') as f:
    data = json.load(f)


fields_list = [
    "TimeStart",
    "TimeEnd",
    "CountContainers",
    "Containers",
    "Cells",
    "Manipulator",
    "Operations"
]
# Update the values in the JSON data
data[fields_list[0]] = 0
data[fields_list[1]] = 3600
data[fields_list[2]] = 4

# Update the Containers array
containers = 3
for ind in range(containers):
    data['Containers'][ind]['content'] = 1
    data['Containers'][ind]['ID'] = 1

# data['Containers'][0]['content'] = 1
# data['Containers'][0]['ID'] = 1
# data['Containers'][1]['content'] = 4
# data['Containers'][1]['ID'] = 2
# data['Containers'][2]['content'] = 4
# data['Containers'][2]['ID'] = 3
# data['Containers'][3]['content'] = 6
# data['Containers'][3]['ID'] = 4

# Update the Cells array
for ind in range(3):
    data['Cells'][ind]['IDCont'] = 3
    
# data['Cells'][0]['IDCont'] = 3
# data['Cells'][1]['IDCont'] = 0
# data['Cells'][2]['IDCont'] = 0

# Update the Manipulator object
data['Manipulator']['condition'] = 0
data['Manipulator']['TimeEnd'] = -1
data['Manipulator']['IDdestination'] = -1
data['Manipulator']['IDcont'] = 0
data['Manipulator']['PPR'] = 3
data['Manipulator']['MotorTime'] = 10000
data['Manipulator']['FreshMotorTime'] = 36

# Update the Operations array
# operations = 7
operations = data['Operations']
operation_names = [operation['Name'] for operation in operations]
print(operation_names)
operation_conditions = [operation['condition'] for operation in operations]
operation_timework = [operation['TimeInWork'] for operation in operations]
operation_prior = [operation['CodePrior'] for operation in operations]
operation_cont = [operation['IDcont'] for operation in operations]
operation_ppr = [operation['PPR'] for operation in operations]
operation_mototime = [operation['MotorTime'] for operation in operations]
operation_newmottime = [operation['FreshMotorTime'] for operation in operations]
operation_runtime = [operation['RunTime'] for operation in operations]
for ind in range(len(operations)):
    data['Operations'][ind]['Name'] = operation_names[ind]
    data['Operations'][ind]['condition'] = operation_conditions[ind]
    data['Operations'][ind]['TimeInWork'] = operation_timework[ind]
    data['Operations'][ind]['CodePrior'] = operation_prior[ind]
    data['Operations'][ind]['IDcont'] = operation_cont[ind]
    data['Operations'][ind]['PPR'] = operation_ppr[ind]
    data['Operations'][ind]['MotorTime'] = operation_mototime[ind]
    data['Operations'][ind]['FreshMotorTime'] = operation_newmottime[ind]
    data['Operations'][ind]['RunTime'] = operation_runtime[ind]

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
