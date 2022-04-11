import json
print("Welcome to supplyManage2 by COSMOS\nType in .help to get started with commands")

initcmd = input("./: ")
while True:
  if initcmd == ".help":
    print(
      "Welcome to supplyManage2\n"
      "Start by creating chain: ./create{}\n"
      "Add product to chain by ./chain/pro\n"
      "Add chain type by: ./chain/type\n"
      "Add destination by: ./chain/desti\n"                 
      "For help with importing a chain: .help.import"
      "Right now, only one chain works. Multiple can be added, but chains will overwrite"
      "Type ./chain/export to export the chain\n"
      "Get started with supplyManage2 now, by COSMOS\n"
      )
    initcmd = input("./: ")
  if initcmd == "./create{}":
    ask = input("Name of Chain: ")
    chain = ask
    chainpro = [] # List of products 
    chaintype = [] # List of Types
    destichain = [] # final place of products
    print("Chain {} is made.".format(chain))
    initcmd = input("./: ")
  
  elif initcmd == "./{}/pro".format(chain):
    productname = input("Name of Product: ")
    chainpro.append(productname)
    initcmd = input("./: ")
  
  elif initcmd == "./{}/type".format(chain):
    typepro = input("Shipping Type: ")
    chaintype.append(chaintype)
    initcmd = input("./: ")
  
  elif initcmd == "./{}/desti".format(chain):
    prodesti = input("Final Place of Product: ")
    destichain.append(prodesti)
    initcmd = input("./: ")
  
  elif initcmd == "./{}/export/pro".format(chain):
    askifexport = input("Do you want to export, y or n: ")
    if askifexport.lower() == 'y':
      print("Exporting Products.")
      with open("DataProducts.txt", 'w') as pro:
        pro.write(json.dumps(chainpro))
        initcmd = input("./: ")
        break
    else:
      initcmd = input("./: ")
  elif initcmd == "./{}/export/type".format(chain):
    askifexport = input("Do you want to export types, y or n: ")
    if askifexport.lower() == 'y':
      with open("DataType.txt", 'w') as type:
        type.write(json.dumps(chaintype))
        break
        initcmd = input("./: ")
    else:
      initcmd = input("./: ")
  elif initcmd == "./{}/export/desti".format(chain):
    askifexport = input("Do you want to export, y or n: ")
    if askifexport.lower() == 'y': 
      with open("DataDesti.txt", 'w') as desti:
        desti.write(json.dumps(destichain))
        break
        initcmd = input("./: ")
    else:
      initcmd = input("./: ")
  elif initcmd == "./import/pro":
   with open('DataProducts.txt', 'r') as readpro:
     imported = readpro.read()
     print(imported)
  elif initcmd == '.help.import':
    print(
      "To read a chain: ./import/products\n"
      "Or: ./import/type\n"
      "Or: ./import/desti\n"
      "Make sure the file is a valid export from the export command."
    )
    initcmd = input("./: ")
  elif initcmd != './create{}' or './{}/pro'.format(chain) or './{}/type'.format(chain) or './{}/desti'.format(chain) or './{}/export'.format(chain) or './import' or '.help' or '.help.import' or './export/pro'.format(chain) or './export/type'.format(chain) or './export/desti'.format(chain) or './import/pro' or './import/type' or './import/desti':
    print("Invalid Command")
    initcmd = input("./: ")
    break
  else:
    print("Invalid Command")
    initcmd = input("./: ")
    break



def print(self, groove):
  groove.self = groove
  groove = 'Welcome to supplyManage2 by COSMOS'
  return groove
