import argparse
import os
import tempfile

SLIDE   = "---"
HEADER = "==="
DEFAULT_OUTPUT = "rule_map"
RULE_KEY = "*gnatcheck rule*"
EXCLUSION_KEY = "*mutually exclusive*"
ENABLE_RULE = "+R"
ANNOTATION = ":"
BUFFER = "-"

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

def add_rule ( standards, title, section_header, rule, isRule):
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
            elif(isRule):
                standards[key] = ( standard, gnatcheck_rule, section_header )
            else:
                standards[key] = gnatcheck_rule.split(",")

def process_one_file ( in_filename, standards, exclusions ):

    lines = []
    with open ( in_filename ) as f:
        lines = f.read().splitlines()

    last_title = ""

    section_header = ""
    for i in range(0,len(lines)):
        if lines[i].startswith ( SLIDE ):
            next = lines[i+1].strip()
            if len(next) > 0:
                last_title = next
        elif lines[i].startswith ( HEADER ):
            cur_section_header = lines[i+1].strip()
            if len(cur_section_header) > 0:
                section_header = cur_section_header
        elif lines[i].lower().startswith ( RULE_KEY ):
            add_rule ( standards, last_title, section_header, lines[i], True )
        elif lines[i].lower().startswith ( EXCLUSION_KEY ):
            add_rule ( exclusions, last_title, section_header, lines[i], False )

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
                        
    parser.add_argument('--params',
                        help='Manually enter params for rules that use them',
                        action='store_true')
                        
    args = parser.parse_args()

    standards = {}
    exclusions = {}

    for root, dirs, files in os.walk ( args.source ):
        for file in files:
            if file.lower().endswith ( ".rst" ):
                process_one_file ( os.path.join ( root, file ), standards, exclusions )

    gnatcheck_rules = find_all_rules()

    rules_file = True
    separator = "_"
    if args.output.lower().endswith("csv"):
        separator = ","
        rules_file = False
    elif args.output.lower().endswith("tab"):
        separator = "\t"
        rules_file = False
    output = open ( args.output, "w" )
   
    commented_rules = {}
    current_header = ""
    for key in sorted(standards.keys()):
        standard = standards[key][0]
        rule = standards[key][1]
        section_header = standards[key][2]
        if (rules_file):
        
           if (section_header != current_header):
              header_buffer = BUFFER * (len(section_header) + 6)
              output.write(header_buffer + "\n")
              output.write("-- " + section_header + " --\n")
              output.write(header_buffer + "\n\n")
              current_header = section_header
        
           commented_out = ""
           white_space = "\n\n"
           param = ""
           if (args.params):
               split_rule = rule.split(":")
               if len(split_rule) > 1:
                  rule = split_rule[0]
                  print("Enter the parameter for rule [" + rule, end="]: ")
                  user_param = input()
                  print()
                  param = ":" + user_param
          
           formatted_text = key + separator + standard.replace(" ", separator)
           if key in exclusions:
              white_space = "\n" 
              num_of_excl_rules = len(exclusions[key])
              for excl_rule in exclusions[key]:
                 commented_rules[excl_rule] = True
                 exclusions.pop(excl_rule)
                 exclusive_rule_text1 = "-- " + key + " is mutually exclusive with the following rule(s): " + ','.join(exclusions[key])
                 exclusive_rule_text2 = "-- " + key + " is active by default. " + ','.join(exclusions[key]) + " is commented out.  Modify rules file as needed."
                 print(exclusive_rule_text1)
                 print(exclusive_rule_text2 + "\n")
                 output.write(exclusive_rule_text1 + "\n")
                 output.write(exclusive_rule_text2 + "\n")
                 
           if key in commented_rules:
              commented_out = "--"
              num_of_excl_rules = num_of_excl_rules - 1
              if num_of_excl_rules == 1:
                 white_space = "\n\n"
                           
              
           output.write (commented_out + ENABLE_RULE + ANNOTATION + formatted_text + ANNOTATION + rule + param + white_space )
           args.short = True
        else:
           output.write ( key + separator + standard + separator + rule + "\n" )
        if rule.lower() in gnatcheck_rules:
            gnatcheck_rules.remove ( rule.lower() )

    if not args.short:
        for rule in gnatcheck_rules:
            output.write ( ' ' + separator + "(unimplemented)" + separator + rule + "\n" )
    output.close()
