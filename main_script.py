#!/usr/bin/env python3

#set the environmnet for the script
import my_function

def main():
    input_name = input("Enter a name: ")

    my_function.greeting(input_name)

#it is main(). or the module being called by something else?

if __name__ == '__main__':
    main()
