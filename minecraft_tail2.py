#!/usr/bin/python
import filetail
import minecraft_commands
import minecraft_tempfile

# default settings
directory = "/home/minecraft/minecraft_ramdisk/"
log_file = "server.log"
ops_file = "ops.txt"
temp_file = "/home/minecraft/scripts/temp_file.txt"

# Make commands object
commands = minecraft_commands.Commander(minecraft_tempfile.read_file(temp_file))
# Set up tail
t = filetail.Tail("%s%s" % (directory, log_file) , only_new = True, max_sleep = 5)
# make ops list
ops_temp = open("%s%s" % (directory, ops_file)).readlines()
ops_list = [i.strip() for i in ops_temp]


print "Current operators:"
for i in ops_list:
    print "\t"+i

# execute commands
while True:
    line = t.nextline()
    line = line.lower()
    l = line.split()
    print "Line is > ", l
    if len(l) < 5:
        print "not enough items"
    else:
        for o in ops_list:
            for c in commands.command_list.keys():
                # Check for matching comannd and confirming individual is in ops_list
                if "<%s> %s" % (o, c) == "%s %s" % (l[3], l[4]):
                    # print commands[c].__doc__
                    commands.command_list[c](o, l)
                    break
                else:
                    pass
