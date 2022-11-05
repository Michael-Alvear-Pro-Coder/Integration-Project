"""this is the main file"""
import vectors as v



if __name__ == "__main__":
    print("This program works as a basic vector calculator, you can add"
          " and subtract vectors, as well as find their magnitudes and "
          "unit vectors\n")



    running = True
    while(running):

        my_x_component = float(input("Enter x component of vector: "))
        my_y_component = float(input("Enter y component of vector: "))

        my_vector = v.Vector((my_x_component, my_y_component))

        print()

        selecting = True
        while(selecting):

            print("select desired computation:\n"
                  "a: add\n"
                  "s: subtract\n"
                  "m: find magnitude\n"
                  "u: find unit vector\n"
                  "q: to quit program\n")

            selection = input()


            if not(selection == "a" or selection == "s" or selection == "m" or
            selection == "u") and selection != "q":

                input("invalid selection try again")

                for i in range(50):
                    print()

            else:

                selecting = False

        if selection == "a":

            new_x_component = float(input("enter the x component of the "
                                        "vector you want to add: "))

            new_y_component = float(input("enter the y component of the "
                                        "vector you want to add: "))


            vector_to_be_added = v.Vector((new_x_component,
                                        new_y_component))

            print("sum vector =", my_vector.get_sum(vector_to_be_added))
            input()

        elif selection == "s":

            new_x_component = float(input("enter the x component of the "
                                        "vector you want to subtract: "))

            new_y_component = float(input("enter the y component of the "
                                        "vector you want to subtract: "))

            vector_to_be_subtracted = v.Vector((new_x_component,
                                        new_y_component))

            print("difference vector =",
                my_vector.get_difference(vector_to_be_subtracted))
            input()

        elif selection == "m":

            print("magnitude =", my_vector.get_magnitude())
            input()

        elif selection == "u":

            print("unit vector =", my_vector.get_unit_vector())
            input()

        elif selection == "q":

            running = False

        for i in range(50):
            print()






    print("program over")