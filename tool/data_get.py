import yaml
def yaml_load():
    with open('../data/data.yaml','r',encoding='utf-8') as f:
         return yaml.load(f)

mylist=[]
print(yaml_load().values())
for i in yaml_load().values():
    mylist.append(tuple(i.values()))
print(mylist)



