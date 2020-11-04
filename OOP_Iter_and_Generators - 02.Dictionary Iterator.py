'''2.	Dictionary Iterator
Create a class called dictionary_iter. Upon initialization it should receive a dictionary object. Implement the iterator,
so it returns each key-value pair of the dictionary as a tuple of two elements (the key and the value).
Note: Submit only the class in the judge system
'''

#dict1=  {3:1, 4:2}
#print(list(dict1.keys())[0])

class dictionary_iter():
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys_list = list(self.dictionary.keys())
        self.key_index = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.key_index >= len(self.keys_list):
            raise StopIteration
        key_index = self.key_index
        self.key_index +=1
        key = self.keys_list[key_index]
        tuple_result = (self.keys_list[key_index], self.dictionary[key] )
        return tuple_result

    def print_index_and_values(self):
        print (self.keys_list)
        #print(self.dictionary[self.key_index[key_index]])

result = dictionary_iter({1: "a", 2: "b"})

#result.print_index_and_values()

for x in result:
  print(x)