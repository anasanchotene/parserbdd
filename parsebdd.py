import argparse

GIVEN = "Dado"
AND = "E"
WHEN = "Quando"
THEN = "Então"

def add_header(nf):
    tf = open("./template", "r")

    for templine in tf:
            nf.write(templine)
    
    tf.close()

    add_new_line(nf)
    add_new_line(nf)

def add_new_line(nf):
    nf.write("\n")

def add_command(nf, text, command):
    text = text.strip(" ").rstrip("\n")

    if "<" in text:
        text = text.replace(text[text.rfind("<"):text.rfind(">")+1], "(.*)")

    nf.write("{0}(/^{1}$/,()=>{{".format(command, text))

    add_new_line(nf)
    add_new_line(nf)
    
    nf.write("})")

    add_new_line(nf)
    add_new_line(nf)

def parse():
    nf = open("./{0}.steps.js".format("sample"), "w")

    add_header(nf)

    f = open("./bdd", "r")
    for line in f:
        line = line.strip(" ")

        if line.startswith(GIVEN):
            add_command(nf, line.split(GIVEN)[1], GIVEN)
        elif line.startswith(AND + " "):
            add_command(nf, line.split(AND + " ")[1], AND)
        elif line.startswith(WHEN):
            add_command(nf, line.split(WHEN)[1], WHEN)
        elif line.startswith(THEN):
            add_command(nf, line.split(THEN)[1], THEN)
        
    f.close()

    nf.flush()
    nf.close()
    print("parse finished")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.parse_args()

    parse()
