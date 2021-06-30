import dropbox
import os

directory = {'/Crypto','/EarningsCalender','/IPO','/Yahoo', '/China'} # TODO auto read in

def connect_to_dropbox():
    TOKEN = 'yxGPhvX_qb4AAAAAAAAAARTSYmp-ajbb6P3YiWsWs6oCF9pQiiKOjoA5k8MFx-bm'
    try:
        dbx = dropbox.Dropbox(TOKEN)
        print('Connected to Dropbox successfully')
    except Exception as e:
        print(str(e))
    return dbx


def updateDirectory():
        try:
            directory=set()
            # dbx object contains all functions that
            # are required to perform actions with dropbox
            files = dbx.files_list_folder('').entries
            print("Reviewing Directory . .. ...")
            for file in files:
                print(file.name)
                directory.add('/'+file.name)
        except Exception as e:
            print(str(e))

        print('directories downloaded :')
        print('=========================')
        for directories in directory:
            print(directories)
        print('=========================')

def list_files_in_folder(folder_path):
    try:
        dbx = connect_to_dropbox()
        files = dbx.files_list_folder(folder_path).entries
        print("------------Listing Files in Folder------------ ")
        for file in files:
            print(file.name)
    except Exception as e:
        print(str(e))


def load(folder_path):
    try:
        files = dbx.files_list_folder(folder_path).entries
        os.mkdir('landingpad'+folder_path)
        for file in files:
            download(folder_path+'/'+file.name, 'landingpad'+folder_path+'/'+file.name)
    except Exception as e:
        print(str(e))


def download(infilePath,outfilePath):
    dbx.files_download_to_file(outfilePath, infilePath)

def grabIndex():
    print('grabbing index')
    try:
        download('/index.csv','landingpad/index.csv')
    except Exception as e:
        print(str(e))

#main code run

list_files_in_folder('/Crypto')
print('[!] Connect to dropbox?')
response = input("(Y/N) : ")
if response == 'Y':
    dbx = connect_to_dropbox()
    updateDirectory()
    grabIndex()
    for directories in directory:
        load(directories)
