class NyaInterpreter():
    def __init__(self, code):
        self.get_code(code);
        self.counter = 0;
        self.result = ''
        self.parse_code()
        print(self.result)

        """
        Fetches the code from a .nya file
        @Params:
            path: str - The Path to the inputed .nya file

        @return
            None
        """
    def get_code(self, path: str):
        with open(path, 'r') as f:
            self.code = f.read().split()

        """
        Reads a character and executes the appropriate action
        @Params:
            char: str - The character which is parsed
                n - Decrements the counter
                y - Increments the counter
                a - Appends the ASCII representation of the counter onto a result which is then printed
                ~ - Resets the counter back to 0
        @return
            None
        """
    def read_char(self, char: str) -> None:
        if char == 'n': self.counter -= 1
        elif char == 'y': self.counter += 1
        elif char == 'a': self.result += chr(self.counter);
        elif char == '~': self.counter = 0
        else: return;


        """
        Iterates through every character within the file and calls the read_char method
        @Params:
            None

        @return:
            None
        """
    def parse_code(self):
        for x in self.code: 
            for i in x:
                self.read_char(i) 

NyaInterpreter('example.nya')

