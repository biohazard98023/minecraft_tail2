#!/usr/bin/python
import filetail
import os

# default settings
directory = "/home/minecraft/minecraft_ramdisk/"
log_file = "server.log"
ops_file = "ops.txt"
screen_invoke_f = "screen -p 0 -S minecraft -X eval 'stuff \""
screen_invoke_b = "\"\\015'"

t = filetail.Tail("%s%s" % (directory, log_file) , only_new = True, max_sleep = 5)

# make ops list
ops_temp = open("%s%s" % (directory, ops_file)).readlines()
ops_list = [i.strip() for i in ops_temp]

for i in ops_list:
    print i


class temp_location(object):

    def __init__(self):
        self.gx = "-1944"
        self.gy = "66"
        self.gz = "-268"

# functions
def home_f(ops_user, command, sf, sb):
    """home_f"""
    x = "-1944"
    y = "66"
    z = "-268"
    cmd = sf + "tp %s %s %s %s" % (ops_user, x, y, z) + sb
    os.system(cmd)

def tstaci_f(ops_user, command, sf, sb):
    """tstaci_f"""
    staci = "SooperKipz"
    cmd = sf + "tp %s %s" % (ops_user, staci) + sb
    os.system(cmd)

def tbob_f(ops_user, command, sf, sb):
    """tbob_f"""
    bob = "Frys_Lower_Horn"
    cmd = sf + "tp %s %s" % (ops_user, bob) + sb
    os.system(cmd)

def tdon_f(ops_user, command, sf, sb):
    """tdon_f"""
    don = "biohazard98023"
    cmd = sf + "tp %s %s" % (ops_user, don) + sb
    os.system(cmd)

def god_f(ops_user, command, sf, sb):
    """god_f"""
    cmd = sf + "gamemode 1 %s" % ops_user + sb
    os.system(cmd)

def mortal_f(ops_user, command, sf, sb):
    """mortal_f"""
    cmd = sf + "gamemode 0 %s" % ops_user + sb
    os.system(cmd)

def temp_f(ops_user, command, sf, sb):
    """temp_f"""
    x = object_dict[ops_user].gx
    y = object_dict[ops_user].gy
    z = object_dict[ops_user].gz
    cmd = sf + "tp %s %s %s %s" % (ops_user, x, y, z) + sb
    os.system(cmd)

def set_temp_f(ops_user, command, sf, sb):
    """set_temp_f"""
    if len(command) < 8:
        print "not enough"
    else:
        object_dict[ops_user].gx = command[5]
        object_dict[ops_user].gy = command[6]
        object_dict[ops_user].gz = command[7]
        x = object_dict[ops_user].gx
        y = object_dict[ops_user].gy
        z =object_dict[ops_user].gz
        cmd = sf + "say temp location x=%s y=%s z=%s" % (x, y, z) + sb
        os.system(cmd)

def current_temp_f(ops_user, command, sf, sb):
    """current_temp_f"""
    x = object_dict[ops_user].gx
    y = object_dict[ops_user].gy
    z = object_dict[ops_user].gz
    cmd = sf + "say %s current temp location x=%s y=%s z=%s" % (ops_user, x, y, z) + sb
    os.system(cmd)

def night_f(ops_user, command, sf, sb):
    """night_f"""
    cmd = sf + "time set 13000" + sb
    os.system(cmd)

def day_f(ops_user, command, sf, sb):
    """day_f"""
    cmd = sf + "time set 0" + sb
    os.system(cmd)

# make location objects
object_dict={}
for i in ops_list:
    vars()[i] = temp_location()
    object_dict[i] = vars()[i]

# commands list
commands = {
    "home" : home_f,
    "tkipz" : tstaci_f,
    "tstaci" : tstaci_f,
    "tbob" : tbob_f,
    "tdon" : tdon_f,
    "god" : god_f,
    "mortal" : mortal_f,
    "temp" : temp_f,
    "set_temp" : set_temp_f,
    "day" : day_f,
    "night" : night_f,
    "current_temp" : current_temp_f
}

# execute commands
while True:
    line = t.nextline()
    line = line.lower()
    l = line.split()
    for o in ops_list:
        for c in commands.keys():
            if len(l) < 5:
                print "not enough items"
            elif "<%s> %s" % (o, c) == "%s %s" % (l[3], l[4]):
                print commands[c].__doc__
                commands[c](o, l, screen_invoke_f, screen_invoke_b)
