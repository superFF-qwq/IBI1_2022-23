## for task2: Triathlon times databaser

class triathlon(object):
    def __init__(self, first_name, last_name, location, swim, cycle, run):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim = swim
        self.cycle = cycle
        self.run = run
        ## time unit : second
    def checkmember(self):
        self.total = self.swim + self.cycle + self.run
        print(self.first_name+' '+self.last_name+' '+self.location+' '+ \
              str(self.swim)+' '+str(self.cycle)+' '+str(self.run)+' '+str(self.total))

champion = triathlon('Hao', 'Miao', 'Spain', 48*60+36, 4*3600+34*60+14, 3*3600+6)
champion.checkmember()