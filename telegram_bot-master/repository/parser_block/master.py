from parser_block.parser import Parser

class Master:
    def __init__(self):
        print("start init parser")
        self.parser = Parser()     

if __name__  == "__main__":
    master = Master()