#Creating a list
My_list= [50,100,150,200,250,300,400,500,800,900]

#adding an element to the list
My_list.append(350)
My_list.insert(0,0)

#Modifying an element in the list
My_list[1]= 70

#Removing an element from the list
My_list.remove(200)
My_list.pop(2)
My_list.pop()
del My_list [-1:]
print("Updated list:", My_list)

Updated list: [0, 70, 150, 250, 300, 400, 500, 800]

#Creating a set
My_set= { 10, 15, 14, 52 ,24,36,367,}

#Adding an element to the set
My_set.add(450)

#Removing an element from the set
My_set.remove(10)
My_set.discard(52)

#Modifying a set element
My_set.discard(14)
My_set.add(82)
My_set.pop()
print("Updated Set:",My_set)

Updated Set: {36, 15, 367, 82, 24}

#Creating a dictionary
My_dict= {'Name':'John','Age':22,'City':'Delhi'}

#Adding an element to dictionary
My_dict['gender']='Male'

#Removing an element from the dictionary
del My_dict['Age']

#Modifying an element in the dictionary
My_dict['City']='Mumbai'
print("Updated Dictionary:", My_dict)

Updated Dictionary: {'Name': 'John', 'City': 'Mumbai', 'gender': 'Male'}
