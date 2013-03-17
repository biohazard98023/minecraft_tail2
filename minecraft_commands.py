# Minecraft_tail2 commands
import os

class Commander (object):

    def __init__(self, custom_commands):
        self.invoke_front = "screen -p 0 -S minecraft -X eval 'stuff \""
        self.invoke_back = "\"\\015'"
        self.custom_commands = custom_commands
        print "custom commands: ", self.custom_commands
        self.command_list = {
            "home" : self.home_f,
            "tkipz" : self.tstaci_f,
            "tstaci" : self.tstaci_f,
            "tbob" : self.tbob_f,
            "tdon" : self.tdon_f,
            "god" : self.god_f,
            "mortal" : self.mortal_f,
            "temp" : self.temp_f,
            "set_temp" : self.set_temp_f,
            "day" : self.day_f,
            "night" : self.night_f,
            "current_temp" : self.current_temp_f,
            "t" : self.t_f,
            "set_t" : self.set_t_f,
            "say_t" : self.say_t_f,
            "chat" : self.chat_t
            }
        
    def home_f(self, ops_user, command):
        """home_f"""
        x = "-1944"
        y = "66"
        z = "-268"
        cmd = self.invoke_front + "tp %s %s %s %s" % (ops_user, x, y, z) + self.invoke_back
        os.system(cmd)
    
    def tstaci_f(self, ops_user, command):
        """tstaci_f"""
        staci = "SooperKipz"
        cmd = self.invoke_front + "tp %s %s" % (ops_user, staci) + self.invoke_back
        os.system(cmd)
    
    def tbob_f(self, ops_user, command):
        """tbob_f"""
        bob = "Frys_Lower_Horn"
        cmd = self.invoke_front + "tp %s %s" % (ops_user, bob) + self.invoke_back
        os.system(cmd)
    
    def tdon_f(self, ops_user, command):
        """tdon_f"""
        don = "biohazard98023"
        cmd = self.invoke_front + "tp %s %s" % (ops_user, don) + self.invoke_back
        os.system(cmd)
    
    def god_f(self, ops_user, command):
        """god_f"""
        cmd = self.invoke_front + "gamemode 1 %s" % ops_user + self.invoke_back
        os.system(cmd)
    
    def mortal_f(self, ops_user, command):
        """mortal_f"""
        cmd = self.invoke_front + "gamemode 0 %s" % ops_user + self.invoke_back
        os.system(cmd)
    
    def temp_f(self, ops_user, command):
        """temp_f"""
        x = object_dict[ops_user].gx
        y = object_dict[ops_user].gy
        z = object_dict[ops_user].gz
        cmd = self.invoke_front + "tp %s %s %s %s" % (ops_user, x, y, z) + self.invoke_back
        os.system(cmd)
    
    def set_temp_f(self, ops_user, command):
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
            cmd = self.invoke_front + "say temp location x=%s y=%s z=%s" % (x, y, z) + self.invoke_back
            os.system(cmd)
    
    def current_temp_f(self, ops_user, command):
        """current_temp_f"""
        x = object_dict[ops_user].gx
        y = object_dict[ops_user].gy
        z = object_dict[ops_user].gz
        cmd = self.invoke_front + "say %s current temp location x=%s y=%s z=%s" % (ops_user, x, y, z) + self.invoke_back
        os.system(cmd)
    
    def night_f(self, ops_user, command):
        """night_f"""
        cmd = self.invoke_front + "time set 13000" + self.invoke_back
        os.system(cmd)
    
    def day_f(self, ops_user, command):
        """day_f"""
        cmd = self.invoke_front + "time set 0" + self.invoke_back
        os.system(cmd)
        
    def t_f(self, ops_user, command):
        for i in self.custom_commands:
            if i.split(" ")[0] == ops_user and i.split(" ")[1] == command[4]:
                cmd = self.invoke_front + "tp %s %s %s %s" % (ops_user, i.split(" ")[2], i.split(" ")[3], i.split(" ")[4]) + self.invoke_back
                os.system(cmd)
            else:
                print "not a match: "
                print "tp %s %s %s %s" % (ops_user, i.split(" ")[2], i.split(" ")[3], i.split(" ")[4])
                print i
            
    def set_t_f(self, ops_user, command):
        pass
    
    def say_t_f(self, ops_user, command):
        pass
    
    def chat_t(self, ops_user, command):
        pass
        