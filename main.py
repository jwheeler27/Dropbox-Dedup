import dropbox
import asyncio
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError, BadInputError

dupes = {}
fileList = {}

def directory_walk(rootDir):
    """Start with root dir that user provides
    and look for subdirectories or files.

    Call ourselves to walk deeper into sub dirs
    otherwise create list of files and dupes.

    Return the list of dupes
    """

    results = dbx.files_list_folder(path=rootDir)
    for i in results.entries:
        if isinstance(i, dropbox.files.FolderMetadata):
            print('Scanning ', i.name + '\n')
            directory_walk(i.path_display)
        else:
            global dupes, fileList
            if i.name in fileList:
                if fileList[i.name][1] == i.size:
                    if fileList[i.name][2] == i.content_hash:
                        dupes[i.name] = (i.path_display, i.size, i.content_hash)
            else:
                fileList[i.name] = (i.path_display, i.size, i.content_hash)

def show_dupes():
    '''Show duplicate filename and path'''
    print('Duplicates found')
    print('----------------')
    for k,v in dupes.items():
        print('Filename: ', k)
        print('Path: ', v[0], '\n')


def move_dupes(tmpDir):
    '''
    Move duplicate files to temp dir for user to manually inspect

    Create file in tempdir with list of original file and path
    '''
    pass

async def delete_dupes():
    '''
    delete duplicate files
    '''
    pass


if __name__ == '__main__':

    # get DropBox OAuth token from user
    # verify able to access account
    TOKEN = input("Type in your access token:\n")

    try:
        dbx = dropbox.Dropbox(TOKEN)
        dbx.users_get_current_account()

    except:
        print('unable to access account, check token')
        quit()

    # scan directory for files and subdirectories
    directory_walk('/Testing')

    if len(dupes) > 0:
        show_dupes()
