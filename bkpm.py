#Burg Kurg Package Manager (bkpm)
import csv
import urllib.request
import sys, getopt
import shutil
import os

version='1.0-alpha'
plugin_dir='/home/pj/FakeServer/plugins'


help_str = f'Burg Kurg Package Manager (bkpm) version {version}\n\nOptions:\n   -i, --install: Install a new package\n   -l, --update-list: Update the package list. You MUST do this first in order to update packages!\n   -u, --update: Update a package\n   -a, --update-all: Update all installed packages\n   -r, --remove: Remove a package\n   -h, --help: Show this help dialog.\n   -s, --source: Specify source for package (Official, Community, Custom)'

print(f"WARNING: bkpm is not complete yet and is still missing several features. It is not ready for production use!")
print(f"Burg Kurg Package Manager version {version}\n")

def main(argv):
    source = 'ALL'
    try:
        opts, args = getopt.getopt(argv,"hi:lu:ar:s:m:",["help","install=","update-list","update","update-all","remove=","source=","manual-install="])
    except getopt.GetoptError:
        print(f'Bad syntax; showing help:\n{help_str}')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print(help_str)
        elif opt in ('-s','--source'):
            if arg.lower() == 'official' or arg == 'community' or arg == 'custom':
                source = arg.lower()
            else:
                print('ERROR: Invalid source. Valid sources are:\nOfficial - Packages come from their developer\'s source\nCommunity - Packages come from a source not owned by the developer\nCustom - Packages come from sources you provide.')
                sys.exit(2)
        elif opt in ('-i','--install'):
            package = arg
            print(f'Searching for {package}...')
            install_pkg(package,source)
        elif opt in ('-l','--update-list'):
            update_db()
        elif opt in ('-u','--update'):
            package = arg
            update_pkg(package,source)
        elif opt in ('-a','--update-all'):
            update_all_pkg()
        elif opt in ('-r','--remove'):
            package = arg
            remove_pkg(package)
        elif opt in ('-m','--manual-install='):
            package = arg
            manual_install(package)
        

#Read list of installed packages...
def read_installed():
    installed = open('installed.csv','r')
    installed_csv = csv.reader(installed)
    for row in installed_csv:
        print(row)

#Update list.csv
def update_db():
    print('Updating list.csv...')
    urllib.request.urlretrieve('https://github.com/PJBeans/bkpm/raw/main/list.csv','./list.csv')
    print('Updating community.csv...')
    urllib.request.urlretrieve('https://github.com/PJBeans/bkpm/raw/main/community.csv','./community.csv')
    print('Finished updating!')

    

#Get description of a given package when using install_pkg
def get_pkg_description(package,row):
    print(f'Name: {row[0]}\nSource: {row[1]}\nAuthor: {row[2]}\nDescription: {row[3]}\nVersion: {row[4]}')

#source = 'ALL' #If no source is provided, default to ALL and check each source until the package is found.

#Install a plugin
def install_pkg(package,source):
    
    installed = open('installed.csv','r')
    installed_csv = csv.reader(installed)
    installed_append = open('installed.csv','a')
    installed_csv_append = csv.writer(installed_append)

    source_list = ['list.csv','community.csv','custom.csv']

    if source == 'ALL':
        goThru = 3 #If no source is specified, search them all.
    else:
        goThru = 1 #By default, search database once.


    if source == 'official':
        database = open('list.csv')

    elif source == 'community':
        database = open('community.csv')
    
    elif source == 'custom':
        database = open('custom.csv')

   
    found = False
    for row in installed_csv:
        if package == row[0]:
            print(f'{package} is already installed.')
            sys.exit(2)
    
    for i in range(0,goThru):
        if goThru != 1:
            database = open(source_list[i])
            database_csv = csv.reader(database)
        else:
            database_csv = csv.reader(database)
        for row in database_csv:
            if package == row[0]:
                print(f'Found {package}!')
                found = True
                get_pkg_description(package,row)
                print(f'Install {package} (y/N)?')
                install_yn = (input('BKPM>')).lower()
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
                    sys.exit(0)
            
    if found == False:
        print(f'ERROR: Could not find {package}. :(')

#Manually add a plugin
def manual_install(package):
    installed = open('installed.csv','a')
    installed_csv = csv.writer(installed)
    print(f'Searching for {package}.')
    if os.path.exists(package):
        package_name = os.path.basename(package) 
        package_name = package_name[:-4].lower() #Remove '.jar' from end of plugin name and make name lowercase, for consistency and to ensure compatibility with the rest of BKPM's features. Since these should all be .jar files, this hard-coded method should be fine.
        print(f'Found {package}.\nWARNING: You\'re responsible for updating this package as it being installed from a local source outside of the BKPM lists.\nInstall {package}? (y/N)?')
        choice = input('BKPM>')
        if choice.lower() == 'y':
            print(f'Moving {package_name} to {plugin_dir}...')
            shutil.move(f'{package}',f'{plugin_dir}/{package_name}.jar')
            print('Saving to installed.csv...')
            newRow = [package_name,'?']
            installed_csv.writerow(newRow)
        else:
            print('Installation aborted!')
    else:
        print(f'ERROR: {package} not found. Please ensure you\'ve entered the complete path to the package!')

#Add to custom.csv

#Update a plugin
def update_pkg(package,source):
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


    #Get database version
    source_list = ['list.csv','community.csv','custom.csv']

    if source == 'ALL':
        goThru = 3 #If no source is specified, search them all.
    else:
        goThru = 1 #By default, search database once.


    if source == 'official':
        database = open('list.csv')

    elif source == 'community':
        database = open('community.csv')
    
    elif source == 'custom':
        database = open('custom.csv')
    

    if found == True:
        for i in range(0,goThru):
            if goThru != 1:
                
                database = open(source_list[i])
                database_csv = csv.reader(database)
            else:
                database_csv = csv.reader(database)
            for row in database_csv:

                if package == row[0] and pkg_version != row[4]:
                    print(f'Update for {package} is available!\n\nCurrent version: {pkg_version}\nNew Version: {row[4]}\n\nUpdate {package} (y/N)?')
                    update_yn = (input('BKPM>')).lower()
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
            #if package not in str(database_lines):      
            #    print(f'ERROR: {package} not found in {source}')
    elif found == False:
        print(f'ERROR: {package} isn\'t installed!')
def update_all_pkg():
    installed = open('installed.csv')
    installed_csv = csv.reader(installed)
    for row in installed_csv:
        if row[0] == "Plugin Name":
            pass
        else:
            update_pkg(row[0],'ALL')

def remove_pkg(package):
    with open('installed.csv','r') as installed:
        installed_csv = csv.reader(installed)
        installed_lines = list(installed_csv)
        found = False
        complete = False
        for i in range(len(installed_lines)):
            #I know this try-except method is pretty janky. I wanna clean this up soon!
            try:
                if package==installed_lines[i][0]:
                    found = True
                    print(f'Are you sure you want to uninstall {package}? (y/N)')
                    uninstall_yn = input('BKPM>')
                    if uninstall_yn == 'y':
                        print(f'Removing {package}...')
                        os.remove(f'{plugin_dir}/{package}.jar')
                        print('Saving to installed.csv...')
                        with open('installed.csv','w') as installed_w:
                            installed_lines.pop(i)
                            installed_csv_writer = csv.writer(installed_w)
                            installed_csv_writer.writerows(installed_lines)
                            complete = True
                    else:
                        print('Nothing was uninstalled.')
            except:
                pass
        if complete == False and found == False:
            print(f'ERROR: {package} is not installed.')


main(sys.argv[1:])


