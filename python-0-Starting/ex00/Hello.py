ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# init my code

# lists are mutable
ft_list[1] = "World!"

# tuples are immutable
ft_tuple = (ft_tuple[0], "Brazil!")

# sets save unique elements
ft_set.remove("tutu!")
ft_set.add("São Paulo!")

# dictionaries are key-value
ft_dict["Hello"] = "42 São Paulo!"

# end my code

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
