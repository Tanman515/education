from package.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Dont work')

if capitalize('') != '':
    raise Exception('Dont work')

print('Work')