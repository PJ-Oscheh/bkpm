#Burg Kurg Package Manager (bkpkg)
import csv
import urllib.request
import sys, getopt
version='1.0-alpha'

print(f"WARNING: bkpkg is not complete yet and is still missing several features. It is not ready for production use!")
print(f"Burg Kurg Package Manager version {version}")

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:",["help","install="])
    except getopt.GetoptError:
        print(f'Bad syntax')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print('Help coming soon!')
        elif opt in ('-i','--install'):
            package = arg
            print(f'Searching for {package}...')
            install_pkg(package)
#Read list of installed packages...
def read_installed():
    installed = open('installed.csv','r')
    installed_csv = csv.reader(installed)
    for row in installed_csv:
        print(row)

#Read list of packages in database...
def update_db():
    database = open('list.csv')
    database_csv = csv.reader(database)
    for row in database_csv:
        print(row)

def get_pkg_description(package,row):
    print(f'Name: {row[0]}\nSource: {row[1]}\nAuthor: {row[2]}\nDescription: {row[3]}\nVersion: {row[4]}')

def install_pkg(package):
    database = open('list.csv')
    database_csv = csv.reader(database)

    found = False
    for row in database_csv:
        if package == row[0]:
            print(f'Found {package}!')
            found = True
            get_pkg_description(package,row)
            print(f'Install {package} (y/N)?')
            install_yn = (input('bkpkg>')).lower()
            if install_yn == 'y':
                print(f'Downloading {row[0]} from {row[1]}...')
                urllib.request.urlretrieve(row[1],f'./download/{row[0]}.jar')
                print(f'Moving {row[0]} to plugins...')
                print('<NOT IMPLEMENTED>')
            else:
                print('Installationg aborted!')
            
    if found == False:
        print(f'ERROR: Could not find {package}. :(')

main(sys.argv[1:])


