
def main():
    print("Given Fictional Flags:")
    print("- User\n- VIP\n- Moderator\n- Admin\n- Developer\n- Bug Hunter\n- Early Tester")
    print("Choose a bitwise flag number.")
    num = int(input("Input here: "))
    flags = []

    if num & 1:
        flags.append("User")

    if num & 2:
        flags.append("VIP")

    if num & 4:
        flags.append("Moderator")

    if num & 8:
        flags.append("Admin")

    if num & 64:
        flags.append("Developer")

    if num & 128:
        flags.append("Bug Hunter")

    if num & 256:
        flags.append("Early Tester")

    if flags == []:
        print("Invalid flag")
        return

    print("--------------------------------------")
    print("Your badges are:\n" + ', '.join(flags))
 
main()