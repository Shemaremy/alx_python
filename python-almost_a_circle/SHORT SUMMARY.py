import json


















#First learn unpacking

a = [1,2,3]
print(a)            #output is [1,2,3]
print(*a)           #output is 1 2 3























# Learn   *Args       (or arguments in parameters with * signs)
def Flacko(a, *m):
    print(m)        # prints everything and excludes first one coz its stored in variable a. 
    print ("first normal arg:  ", a)
    for arg in m:                     # m here is being considered as an array
        print ("another arg:       ", arg)

Flacko('one','two','three','four')     #Here, one is assigned to a(first argument) and the remainings will be stored in *m. Pass multiple values to one variable



























#  Learn  *kwargs       (or arguments in parameters with ** signs)
''' Probably, **kwargs accept  keyword arguments while *args don't. As we have seen above,
    we were passing arguments with no keys. **kwargs allows you to do so   '''

def Blue(a, **m):
    print("First kwarg: ", a)
    
    for i in m:
         print("Other kwargs: ", m)

Blue("Flacko", Age=32, Location="USA", Kids=2)    # DISCLAIMER!!! The first argument never has to have a key! Else, you get an error  



 

























# Learn         JSON (Java Script Object Notation)
'''
- DISCLAIMER!!          (    THE FIRST RULE IS TO IMPORT JSON FROM THE ABOVE        )
- Same syntax as the dictionary, don't worry.
- The keyword JS doesnt count in json, its because it was based on javascript

* Used for
    - Configuration files,      - Storing Data,     -API's

* We'll know how to
    (i) Change JSON dictionary data to python         (Decode)
           > syntax of a json container below in green
'''          
#             ------------>   a = '''{"ibindanga:"[{":"}]}'''    <-------------------
'''    
    
    
    (ii) Change Python dictionary data to JSON          (Encode)
    

'''




# (i)  ENCODE      (We use dumps)      python to json
#python dictionary
a2 = {
    
            "Ibindanga":     [   {"Name": "Remy", "Age": 21, "Loc": "Taiwan"}   ]
        
        } 


d2 = json.dumps(a2)
print(d2)           #{"Ibindanga": [{"Name": "Remy", "Age": 21, "Loc": "Taiwan"}]}




#   ii) DECODE   (We use loads)  :   json to python
a = '''{
    
            "Ibindanga":     [   {"Name": "Remy", "Age": 21, "Loc": "Taiwan"}   ]
        
        }'''
# The reason why we put the data in (''') is because the json data must be a sting / documented as (''')
d = json.loads(a)
print(d)                    # output : {'Ibindanga': [{'Name': 'Remy', 'Age': 21, 'Loc': 'Taiwan'}]}





'''
The only difference between the decode and encode output is that
- in the encode output is ("")
- in the decode the output comes in the ('')

'''











