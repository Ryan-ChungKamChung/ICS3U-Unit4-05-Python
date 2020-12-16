#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Program adds inputted numbers through input loops


def main():
    # this function adds inputted numbers through input loops

    while True:
        # Input
        number_of_inputs_string = input("Please enter how many numbers you"
                                        " would like to add together: ")

        try:
            number_of_inputs = int(number_of_inputs_string)

            assert number_of_inputs > 0

            break

        except AssertionError:
            print("This isn't a valid input")
        except Exception:
            print("This isn't a valid input")

    sum = 0
    loop_counter = 0

    # Input
    while loop_counter < number_of_inputs:
        loop_counter = loop_counter + 1

        # Input
        while True:
            input_number_string = input("Please enter an integer to add: ")

            try:
                input_number = int(input_number_string)
                assert input_number > 0
                break
            except AssertionError:
                print("This isn't a valid input")
            except Exception:
                print("This isn't a valid input")

        sum = sum + input_number

        if loop_counter < number_of_inputs:
            continue

        print("The sum of all positive numbers is: {}".format(sum))


if __name__ == "__main__":
    main()
