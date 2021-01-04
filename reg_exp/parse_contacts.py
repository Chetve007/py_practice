import re

regexp = re.compile(r"(?P<last>[-a-zA-Z]+)"  # фамилия и запятая
                    r" (?P<first>[-a-zA-Z]+)"  #  имя
                    r"( (?P<middle>([-a-zA-Z]+)))?"  # необязательное отчество
                    r": (?P<phone>(\d{3}-\d{3}-\d{4}))"  # двоеточие и телефон
                    )

file = open('./reg_exp/contacts.txt')
for line in file.readlines():
    result = regexp.search(line)
    if result == None:
        print("Oops, I don't think this is a record")
    else:
        lastname = result.group('last')
        firstname = result.group('first')
        middlename = result.group('middle') if result.group('middle') else ''
        phonenumber = result.group('phone')
        print(f'Name: {firstname} {middlename} {lastname}, Number: {phonenumber}')

file.close()
