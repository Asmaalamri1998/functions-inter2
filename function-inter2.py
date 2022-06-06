x = [ [5,2,3], [10,8,9] ]
x[1][0]=15
print(x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']='Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(stu) :
    
    for x in range(0,len(stu)):
        k= list(stu[x].keys())
        v=list(stu[x].values())
        sen_print=""
        for i in range(0,len(k)-1):
            sen_print+=(f"{k[i]}-{v[i]},")
            sen_print+=(f"{k[len(k)-1]}-{v[len(v)-1]}")
            print(sen_print)


def iterateDictionary2(key_name, some_list):
    k = key_name
    for x in range(0,len(some_list)):
        print(some_list[x][k])
print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))

    
print(iterateDictionary(students))  


def printInfo(some_dict):
    for x in some_dict:
        print(len(some_dict[x]),x)
        for i in some_dict[x]:
            print(i)
        print('')

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(printInfo(dojo))


