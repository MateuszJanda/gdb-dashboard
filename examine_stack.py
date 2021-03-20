import gdb

# https://sourceware.org/gdb/onlinedocs/gdb/Commands-In-Python.html#Commands-In-Python


ITEM_SIZE = 4  # for 32 bit architecture
# ITEM_SIZE = 8  # for 64 bit architecture


class ExamineStack32(gdb.Command):
    def __init__(self):
        """This registers our class as 'examine_stack_32'"""
        super(ExamineStack32, self).__init__("examine_stack_32", gdb.COMMAND_DATA)

    def invoke(self, num_of_items, from_tty):
        # When we call "command" from gdb, this method is called
        for i in range(0, int(num_of_items) * ITEM_SIZE, ITEM_SIZE):
            gdb.execute('printf "Examine $esp+' + str(i) + ': 0x%0x\\n", $esp+' + str(i))
            try:
                gdb.execute("x/x $esp+" + str(i))
                gdb.execute("info symbol *(int*)($esp+" + str(i) + ")")
            except Exception as _:
                print("Can't access: $esp+" + str(i))


ExamineStack32()
