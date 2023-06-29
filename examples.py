from flask import Flask,session

app = Flask(__name__)

#Data structures in python

#List datastructure
my_list = [1, 2, "raman", "sai", True]
my_list.append(2)

#how to create, initianlise the list
#In how many way can we create a list, 
#How to create a List with default values.
#how to iterate the list
#how to add an element in list
#how to show an element in list
#how to delete an element
#how to display a small portion in the list

####
###   WHAT IS MUTABILITY/IMMUTABILITY
#####

#tuple
my_tuple = (1, 2, 3, 4, ("name", "hearaman"))

#Sets

my_set = set()
my_set.add(1)

#Dictionary
my_dict = {"name": "heraaman", "age": 35, "company": "Target"}

#Array

#String
my_name="hearaman"


@app.route('/posts')
def param_example1():
   
    return 'list of posts'

@app.route('/posts/<int:post_id>')
def param_example2(post_id):
   
    return 'Going to tirupati. my post id '+ str(post_id)

if __name__=="__main__":
    app.run(debug=True)