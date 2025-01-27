class Register:
    def __init__(self):

        self.V = [0] * 16
        self.VF=0
        self.I = 0
        self.pc = 0x200
        self.stack = []  # the stack can hold up to 16 16-bit values
        self.sp = 0
        self.delay_timer = 0
        self.sound_timer = 0
        self.key = [0] * 16
