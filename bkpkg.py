#Burg Kurg Package Manager (bkpkg)
import csv
import urllib.request
import sys, getopt
import shutil

version='1.0-alpha'
plugin_dir=''


print(f"WARNING: bkpkg is not complete yet and is still missing several features. It is not ready for production use!")
print(f"Burg Kurg Package Manager version {version}\n")

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:lu:a",["help","install=","update-list","update","update-all"])
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
        elif opt in ('-l','--update-list'):
            update_db()
        elif opt in ('-u','--update'):
            package = arg
            update_pkg(package)
        elif opt in ('-a','--update-all'):
            update_all_pkg()
#Read list of installed packages...
def read_installed():
    installed = open('installed.csv','r')
    installed_csv = csv.reader(installed)
    for row in installed_csv:
        print(row)

#Update list.csv
def update_db():
    print('Updating list.csv...')
    urllib.request.urlretrieve('https://github.com/PJBeans/bkpkg/raw/main/list.csv','./list.csv')
    print('Finished updating!')

    

#Get description of a given package when using install_pkg
def get_pkg_description(package,row):
    print(f'Name: {row[0]}\nSource: {row[1]}\nAuthor: {row[2]}\nDescription: {row[3]}\nVersion: {row[4]}')

#Install a plugin
def install_pkg(package):
    database = open('list.csv')
    database_csv = csv.reader(database)
    installed = open('installed.csv','r')
    installed_csv = csv.reader(installed)
    installed_append = open('installed.csv','a')
    installed_csv_append = csv.writer(installed_append)

    found = False
    for row in installed_csv:
        if package == row[0]:
            print(f'{package} is already installed.')
            sys.exit(2)
    for row in database_csv:
        if package == row[0]:
            print(f'Found {package}!')
            found = True
            get_pkg_description(package,row)
            print(f'Install {package} (y/N)?')
            install_yn = (input('BKPKG>')).lower()
            if install_yn == 'y':
                print(f'Downloading {row[0]} from {row[1]}...')
                urllib.request.urlretrieve(row[1],f'./download/{row[0]}.jar')
                print(f'Moving {row[0]}.jar to {plugin_dir}...')
                shutil.move(f'./download/{row[0]}.jar',f'{plugin_dir}/{row[0]}.jar')
                print('Saving to installed.csv...')
                newRow = [row[0],row[4]]
                installed_csv_append.writerow(newRow)
            else:
                print('Installation aborted!')
            
    if found == False:
        print(f'ERROR: Could not find {package}. :(')

#Update a plugin
def update_pkg(package):
    database = open('list.csv')
    database_csv = csv.reader(database)
    installed = open('installed.csv','r')
    installed_csv = csv.reader(installed)
    #installed_write = open('installed.csv','w')
    #installed_write_csv = csv.reader(installed_write)
    found = False
    print(f'Checking if {package} can be updated...')
    #Get currently installed version
    for row in installed_csv:
        if package == row[0]:
            pkg_version = row[1]
            found = True
    #Get list.csv version
    if found == True:
        for row in database_csv:
            if package == row[0] and pkg_version != row[4]:
                print(f'Update for {package} is available!\n\nCurrent version: {pkg_version}\nNew Version: {row[4]}\n\nUpdate {package} (y/N)?')
                update_yn = (input('BKPKG>')).lower()
                if update_yn == 'y':
                    pkg_version_new = row[4]
                    print(f'Downloading {row[0]} from {row[1]}...')
                    urllib.request.urlretrieve(row[1],f'./download/{row[0]}.jar')
                    print(f'Moving {row[0]}.jar to {plugin_dir}...')
                    shutil.move(f'./download/{row[0]}.jar',f'{plugin_dir}/{row[0]}.jar')
                    print('Saving to installed.csv...')
                    

                    i = 0 #Since CSV rows make for loops wonky, we manually set up our iteration.
                    installed = open('installed.csv','r') 
                    installed_csv = csv.reader(installed)
                    for row in installed_csv:
                        if package == row[0]:
                            newRow = [row[0],pkg_version_new]
                            installed = open('installed.csv','r') 
                            installed_csv = csv.reader(installed)
                            installed_lines = list(installed_csv)
                            installed_lines[i][1] = pkg_version_new
                            installed_write = open('installed.csv','w')
                            installed_write_csv = csv.writer(installed_write)
                            installed_write_csv.writerows(installed_lines)

                        else:
                            i+=1
            elif package == row[0] and pkg_version == row[4]:
                print(f'{package} is up to date.')
    elif found == False:
        print(f'ERROR: {package} isn\'t installed!')

def update_all_pkg():
    installed = open('installed.csv')
    installed_csv = csv.reader(installed)
    for row in installed_csv:
        if row[0] == "Plugin Name":
            pass
        else:
            update_pkg(row[0])

main(sys.argv[1:])


