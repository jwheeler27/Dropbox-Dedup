import dropbox
import sys
import asyncio
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError, BadInputError


def directoryWalk(rootDir):
    """Start with root dir that user provides
    and look for subdirectories or files.

    Call ourselves to walk deeper into sub dirs
    otherwise create list of files and dupes.

    Return the list of dupes
    """


if __name__ == '__main__':

    TOKEN = input("Type in your access token:\n")

    dbx = dropbox.Dropbox(TOKEN)

    directoryWalk('/Testing')
