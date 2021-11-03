import argparse
import os

SLIDE   = "---"
DEFAULT_OUTPUT = "rule_map.tab"
RULE_KEY = "*gnatcheck rule*"

def get_gnatcheck_rule ( rule ):
    last_space = rule.rindex(' ')
    if last_space < 0:
        return ""
    else:
        return rule[last_space:]

def get_standard ( title ):
    right_paren = title.rindex(')')
    left_paren = title.rindex('(')
    key = title[left_paren+1:right_paren]
    standard = title[0:left_paren].strip()
    return ( key, standard )


def add_rule ( standards, title, rule ):
    if len(title) == 0:
        print ( "No title for '" + rule + "'" )
    elif title in standards.keys():
        print ( "Title '" + title + "' already found" )
    else:
        gnatcheck_rule = get_gnatcheck_rule ( rule )
        if len(gnatcheck_rule) == 0:
            print ( "'" + rule + "' is not a legal rule format" )
        else:
            key, standard = get_standard ( title )
            if len(key) == 0 or len(standard) == 0:
                print ("'" + title + "' is not a legal standard format" )
            else:
                standards[key] = ( standard, gnatcheck_rule )

def process_one_file ( in_filename, standards ):

    lines = []
    with open ( in_filename ) as f:
        lines = f.read().splitlines()

    last_title = ""

    for i in range(0,len(lines)):
        if lines[i].startswith ( SLIDE ):
            next = lines[i+1].strip()
            if len(next) > 0:
                last_title = next
        elif lines[i].lower().startswith ( RULE_KEY ):
            add_rule ( standards, last_title, lines[i] )

if __name__== "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--guidelines',
                        help='directory containing source files for guidelines (will be searched recursively)',
                        required=True)

    parser.add_argument('--output',
                        help='Filename for generated map.' +
                             'Extension of CSV for comma-separated, TAB for tab-separated.' +
                             'Default = ' + DEFAULT_OUTPUT,
                        default=DEFAULT_OUTPUT)

    args = parser.parse_args()

    standards = {}

    for root, dirs, files in os.walk ( args.guidelines ):
        for file in files:
            if file.lower().endswith ( ".rst" ):
                process_one_file ( os.path.join ( root, file ), standards )

    separator = "\t"
    if args.output.lower().endswith("csv"):
        separator = ","
    output = open ( args.output, "w" )
    for key in sorted(standards.keys()):
        output.write ( key + separator + standards[key][0] + separator + standards[key][1] + "\n" )
    output.close()
