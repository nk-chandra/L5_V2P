import pyeapi,os,yaml

pyeapi.load_config('eapi.conf')
file = open('switches.yml')
sw_dict = yaml.safe_load(file)
directory = 'configs'

if not os.path.exists(directory):
    os.makedirs(directory)

#switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3', 'spine4', 'borderleaf1', 'borderleaf2']

for sw in sw_dict['switches']:
    connect = pyeapi.connect_to(sw)
    running_config = connect.get_config(as_string='True')
    path = directory + '/' + sw + '.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print('Backing up ' + sw)
