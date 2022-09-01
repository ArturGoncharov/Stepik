class Bim():
    say = 'I love bim'

a = 'Before introducing classes I first have to tell you something about Pythons scope rules\n' \
    'Class definitions play some neat tricks with namespaces and you need to know how scopes\n' \
    'and namespaces work to fully understand whats going on\n' \
    'Incidentally knowledge about this subject is useful for any advanced Python programmer\n' \
    'Lets begin with some definitions\n' \
    'A namespace is a mapping from names to objects\n' \
    'Most namespaces are currently implemented as Python dictionaries but thats normally\n' \
    'not noticeable in any way The important thing to know about namespaces is that\n' \
    'there is absolutely no relation between names in different namespaces' \

b = 'Namespaces are created at different moments and have different lifetimes\n' \
    'The namespace containing the builtin names is created\n' \
    'when the Python interpreter starts up and is never deleted\n' \
    'The global namespace for a module is created when the module definition is read in\n' \
    'normally module namespaces also last until the interpreter quits\n' \
    'The statements executed by the toplevel invocation of the interpreter\n' \
    'either read from a script file or interactively are considered part of a module called __main__\n' \
    'so they have their own global namespace\n' \
    'The builtin names actually also live in a module this is called builtins\n' \

names_1 = []
n = 1
for name in set(a.split()):
    name = name + str(n)
    names_1.append(name)
    n += 1

names_2 = []
n = 1
for name in set(b.split()):
    name = name + str(n)
    names_2.append(name)
    n += 1

for name in names_1:
    exec name + ' = Bim()'

for name1 in names_1:
    for name2 in names_2:
        if 'i' in name2:
            exec name2 + ' = ' + name1