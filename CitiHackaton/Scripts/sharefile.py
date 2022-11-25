import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
from dropbox.sharing import CreateSharedLinkArg

Token = "sl.BTvss6XkiZG1TkXySBL6Sm3FVphoi72fuNxZg0i7nVyy4yyjVvNr29wff0mn_tl_mBVTRDFjAC-rjAiVd84nlEZbJam3YXlTjpsO3uspZ0ngVCIYIBLeXgcj_rjFVDijKZLgQRg"

def backup(dbx, Localfile, Backuppath):

    with open(Localfile, "rb") as f:

        try:
            dbx.files_upload(f.read(), Backuppath, mode=WriteMode("overwrite"))
            result = dbx.sharing_create_shared_link_with_settings(path=Backuppath)
            return result.url
        except ApiError as err:
            if(err.error.is_path1() and err.error.get_path().error.is_insufficient_space()):
                sys.exit("Insufficient space")
            elif err.user_message_text:
                print(err)
                sys.exit()
            else:
                print(err)
                sys.exit()

def upload(Localfile, Backuppath):

    if (len(Token)==0):
        sys.exit("Add access token")

    dbx=dropbox.Dropbox(Token)

    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit("Invalid Token")

        url = backup(dbx, Localfile, Backuppath)
        return url