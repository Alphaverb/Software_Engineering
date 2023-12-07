def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()

            if not data:
                raise Exception("Файл пустой")
            else:
                print(data)

    except Exception as e:
        print(e)

read_file('empty.txt')
read_file('full_of_information.txt')
