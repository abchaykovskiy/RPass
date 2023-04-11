import random 

class RPassword:
    """Main class for simple solution - generate random password."""
    
    def __init__(self):
        self.chars = '+-/*!&$#@?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


    def greet_user(self):
        msg = '# ' * 30 + '\n' + 'Welcome to RPass! Easy passwords for everyone!' + '\n' + '# '*30
        return msg

    
    def say_goodbye(self):
        msg = '# ' * 30 + '\n' + 'Bye! Already miss you!' + '\n' + '# '*30
        return msg


    def take_number(self):
        """Ask user how many passwords required."""
        while 1:
            try:
                cont = int(input('Number of passwords (whole number): '))
                return cont
            except ValueError as va:
                print('Please enter correct number or 0 to exit!')


    def take_length(self):
        """Ask user how long password is required."""
        while 1:
            try:
                length = int(input('Length of password (whole number): '))
                return length
            except ValueError as va:
                print('Please enter correct number or 0 to exit!')


    def generate_password(self, number, length):
        """Gen part"""
        pass_list = []
        for x in range(number):
            password = ''            
            for y in range(length):
                letter = random.choice(self.chars)
                while not password and letter in ('1234567890'):
                    letter = random.choice(self.chars)
                password += letter
            pass_list.append(password)
        return pass_list



    def gen(self):
        """Main loop of program."""
        while 1:
            # Sayng 'Hello' to user.
            print(self.greet_user())

            # Question 1
            number = self.take_number()
            if number == 0:
                return

            # Question 2
            length = self.take_length()
            if length == 0:
                return

            # Password generation part.
            pass_list = self.generate_password(number, length)
            
            # writing to file
            with open('Passwords.txt', 'a') as f:
                for p in pass_list:
                    f.write('\n' + p)

            # Finalization part.
            while 1:
                finish_msg = input('One more try? y/n :')
                match finish_msg.lower():
                    case 'y':
                        break
                    case 'n':
                        print(self.say_goodbye())
                        return


c = RPassword()
c.gen()