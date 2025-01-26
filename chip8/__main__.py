
class Memory:
    """The Chip-8 has 4KB of memory in total, which is 4096 bytes."""
    # From 0x000 to 0x1FF, the interpreter itself occupies the first 512 bytes of memory.
    # From 0x200 to 0xFFF, programs can be stored in memory. The Chip-8 interpreter itself uses only the first 512 bytes of memory, 
    # in the system memory map, and programs should not overwrite those memory locations.
    def __init__(self):
        self.memory = [0] * 4096
