def greetUser(name,years):

    if years < 10:
        role='Software developer'
    else:
        role='Lead Engineer'
    print("Welcome {name}.Your role in this project is {role}".format(name=name,role=role))