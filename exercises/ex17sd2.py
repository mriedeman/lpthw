from sys import argv
#from os.path import exists

script, from_file, to_file = argv



ff = open(from_file)
out_file = open(to_file, 'w')


out_file.write(ff.read())


out_file.close()
ff.close()


