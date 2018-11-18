import pandas as pd
import shutil

dirList = ['aiua120214-0', 'aiua120214-1', 'aiua120214-2', 'aiua120306-0', 'aiua120306-1']
speedLimitTags = ['speedLimit', 'SpeedLimit', 'rampSpeed']
filenameTags = {}
filenameTags['Filename'] = []
filenameTags['Annotation tag'] = []

for dir in dirList:
    csv_df = pd.read_csv('./' + dir + '/frameAnnotations.csv', sep=';')
    for index, row in csv_df.iterrows():
        filename = row['Filename']
        tag = row['Annotation tag']


        if any(speedLimitTag in tag for speedLimitTag in speedLimitTags):
            filenameTags['Filename'].append(filename)
            filenameTags['Annotation tag'].append(tag[-2:])

usefulFiles = pd.DataFrame(filenameTags)
usefulFiles = usefulFiles.sort_values(by=['Annotation tag'])

newFilenames = {}
newFilenames['Filename'] = []
newFilenames['Annotation tag'] = []

for idx, row in usefulFiles.iterrows():
    filename = row['Filename']
    tag = row['Annotation tag']
    try:
        newFilename = 'image' + str(idx) + '.png'
        shutil.copy('./images/' + filename, './useful_images/' + newFilename)
        newFilenames['Filename'].append(newFilename)
        newFilenames['Annotation tag'].append(tag)
    except:
        usefulFiles.drop(idx)

usefulFiles = pd.DataFrame(newFilenames)
usefulFiles.to_csv('speedLimit.csv', sep=',', encoding='utf-8')
