import time

for i in range(100000):
    if i % 5 == 0 or i % 5 == 2 or i % 5 == 3:
        for k in range(5):
            print("\033[41m{}".format("            "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            print("\033[41m{}".format("   ") + "\033[44m{}".format("      ") + "\033[41m{}".format("   "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            print("\033[41m{}".format("   ") + "\033[41m{}".format("      ") + "\033[41m{}".format("   "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            print("\033[41m{}".format("            "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            print("\033[41m{}".format("  ") + "\033[47m{}".format("        ") + "\033[41m{}".format("  "), end="\033[47m{}".format("   "))
        print()
        print()
    if i % 5 == 1:
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("            "), end="\033[47m{}".format("   "))
            else:
                print("\033[44m{}".format("            "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("   ") + "\033[44m{}".format("      ") + "\033[41m{}".format("   "),
                      end="\033[47m{}".format("   "))
            else:
                print("\033[44m{}".format("   ") + "\033[40m{}".format("      ") + "\033[44m{}".format("   "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("            "), end="\033[47m{}".format("   "))
            else:
                print("\033[44m{}".format("            "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("            "), end="\033[47m{}".format("   "))
            else:
                print("\033[44m{}".format("            "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("  ") + "\033[47m{}".format("        ") + "\033[41m{}".format("  "),
                      end="\033[47m{}".format("   "))
            else:
                print("\033[44m{}".format("  ") + "\033[47m{}".format("        ") + "\033[44m{}".format("  "), end="\033[47m{}".format("   "))
        print()
        print()
    if i % 5 == 4:
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("            "), end="\033[47m{}".format("   "))
            else:
                print("\033[47m{}".format("            "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("   ") + "\033[44m{}".format("      ") + "\033[41m{}".format("   "),
                      end="\033[47m{}".format("   "))
            else:
                print("\033[47m{}".format("   ") + "\033[47m{}".format("      ") + "\033[47m{}".format("   "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("            "), end="\033[47m{}".format("   "))
            else:
                print("\033[47m{}".format("            "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("            "), end="\033[47m{}".format("   "))
            else:
                print("\033[47m{}".format("            "), end="\033[47m{}".format("   "))
        print("\033[47m{}".format("                                                                        "))
        for k in range(5):
            if k == 0 or k == 4:
                print("\033[41m{}".format("  ") + "\033[47m{}".format("        ") + "\033[41m{}".format("  "),
                      end="\033[47m{}".format("   "))
            else:
                print("\033[47m{}".format("  ") + "\033[47m{}".format("        ") + "\033[47m{}".format("  "), end="\033[47m{}".format("   "))
        print()
        print()
        time.sleep(1.42069)
        for e in range(6):
            print()
