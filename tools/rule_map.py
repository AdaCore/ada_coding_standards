import argparse
import os
import tempfile

SLIDE   = "---"
DEFAULT_OUTPUT = "rule_map.tab"
RULE_KEY = "*gnatcheck rule*"

def get_gnatcheck_rule ( rule ):
    last_space = rule.rindex(' ')
    if last_space < 0:
        return ""
    else:
        return rule[last_space:].strip()

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

def find_all_rules():
    gnatcheck_rules = []
    temp = tempfile.NamedTemporaryFile()
    temp.close()
    os.system ( "gnatcheck -h 2> " + temp.name )
    with open ( temp.name, 'r' ) as file:
        for line in file:
            if len(line) > 0 and line[0] == ' ' and ' - ' in line:
                gnatcheck_rules.append (line.strip().split(' ')[0].lower() )
    os.remove ( temp.name )
    return gnatcheck_rules

if __name__== "__main__":

    parser = argparse.ArgumentParser(description='Generate a table that maps coding standards to "gnatcheck" rules')

    parser.add_argument('--source',
                        help='Directory containing source files for guidelines (will be searched recursively)',
                        required=True)

    parser.add_argument('--output',
                        help='Filename for generated map.' +
                             'Extension of CSV for comma-separated, TAB for tab-separated.' +
                             'Default = ' + DEFAULT_OUTPUT,
                        default=DEFAULT_OUTPUT)

    parser.add_argument('--short',
                        help='Do not show unimplemented "gnatcheck" rules',
                        action='store_true')

    args = parser.parse_args()

    standards = {}

    for root, dirs, files in os.walk ( args.source ):
        for file in files:
            if file.lower().endswith ( ".rst" ):
                process_one_file ( os.path.join ( root, file ), standards )

    gnatcheck_rules = find_all_rules()

    separator = "\t"
    if args.output.lower().endswith("csv"):
        separator = ","
    output = open ( args.output, "w" )
    for key in sorted(standards.keys()):
        standard = standards[key][0]
        rule = standards[key][1]
        output.write ( key + separator + standard + separator + rule + "\n" )
        if rule.lower() in gnatcheck_rules:
            gnatcheck_rules.remove ( rule.lower() )

    if not args.short:
        for rule in gnatcheck_rules:
            output.write ( ' ' + separator + "(unimplemented)" + separator + rule + "\n" )
    output.close()
