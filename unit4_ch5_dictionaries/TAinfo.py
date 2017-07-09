#We've defined a list of tuples below. Each tuple follows
#the format: (name, home state).
#
#Create a dictionary called ta_dict in the space below, where
#the keys are each TA's name, and the values are their home
#state.

ta_info = [("Joshua", "Georgia"),
          ("Jackie", "Vermont"),
          ("Marguerite", "Tennessee")]

#Add your code to create the dictionary as described!
#The first item in each tuple should be a key, and
#the second item in each tuple should be its value.
#Note that you may create this either by reading and
#using the ta_info list of tuples, or you can create
#the dictionary from scratch:


#Create your dictionary here!
ta_dict = {}
for info in ta_info:
    ta_dict[info[0]] = info[1]

#Now, create three variables: josh_val, jack_val, and
#marg_val. Set josh_val equal to Josh's dictionary value,
#then jack_val equal to Jackie's, then marg_val equal to
#Marguerite's. Remember how to properly access the value
#corresponding to a dictionary key!
#
#Make sure you use dictionary-access syntax to do this.
#Don't create the variables based on new values.


#Create your variables here!
josh_val = ta_dict["Joshua"]
jack_val = ta_dict["Jackie"]
marg_val = ta_dict["Marguerite"]


#If your code works as intended, the following three lines
#will run and print Georgia, Vermont, and Tennessee:
print(josh_val)
print(jack_val)
print(marg_val)




