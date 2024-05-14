import shutil, os

#deletes tempory file
def delete_temp_files():
    folder = "C:\\WINDOWS\\Temp"

    shutil.rmtree(folder, ignore_errors=True)
    print(f"Contents of {folder} has been deleted SUCCESSFULLY!")

#def delete_cache_file():
    
#def delete_old_restore_points():

#def delete_windows_update():

#def delete_log_reports():

#def delete_unused_apps():

#def delete_large_files():

#def empty_recycle_bin():

#def delete_old_downloads():

#def delete_browser_cookies():

delete_temp_files()