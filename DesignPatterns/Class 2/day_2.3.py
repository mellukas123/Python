class Input:
    html_tag = ""

    def get_html(self):
        return self.html_tag

class Submit(Input):
    html_tag = "<input type='submit'></input>"

class Radio(Input):
    html_tag = "<input type='radio'></input>"

class Check(Input):
    html_tag = "<input type='check'></input>"


class Multiselect(Input):
    html_tag = "<input type='multiselect'></input>"

class InputFactory:
    def create_input(self, type):
        target_class = type.capitalize() # if type will be "check" ==> "Check" after capitalizing
        return globals()[target_class]() # example: target_class = Check,so in here we will have Check()

input_factory = InputFactory()

inputs = ['submit', 'radio', 'check', 'multiselect']

for i in inputs:
    print(input_factory.create_input(i).get_html())
3