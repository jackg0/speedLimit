'''
Finds images with traffic sign labels in json files of 'bdd100k', a dataset made by Berkeley Deep Drive.
'''
import ijson, string, sys, getopt, csv

def findImages(json_file):

    json_file = open(json_file)
    items = ijson.items(json_file, 'item')

    relevant_files = []

    for item in items:
        for label in item['labels']:
            if label['category'] == 'traffic sign':
                relevant_files.append(item['name'])
                break

    with open('image_list.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerow(relevant_files)

if __name__ == '__main__':

    try:
       opts, args = getopt.getopt(sys.argv[1:],'h:f:')
    except getopt.GetoptError:

        print ('opts:')
        print (opts)

        print ('\n')
        print ('args:')
        print (args)

        print ('Incorrect usage of command line: ')
        print ('python traffic_sign_finder.py -f <file>')

        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('python traffic_sign_finder.py -f <file>')
            sys.exit()
        elif opt in ('-f'):
            json_file = arg

    findImages(json_file)
