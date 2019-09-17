print("hello world!")
hello_list = ["Hello", "this", "is", "a", "list"]
hello_dict = {"firstName": "Suryadip",
              "lastName": "Bandyopadhyay",
              "eyeColor": "black"}
hello_tuple = (21, 32)
print(hello_list[4])
hello_list[4] += "!"
print(hello_list[4])
print(hello_tuple[0])

print("{0} {1} has {2} eyes.".format(hello_dict["firstName"],
                                     hello_dict["lastName"],
                                     hello_dict["eyeColor"]))
