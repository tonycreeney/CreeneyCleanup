import shutil

#deletes tempory file
def delete_temp_files():
    file = "C:\\WINDOWS\\Temp\\"

    #trys to remove the error, if it fails, it displays the error for you to read
    try:    
        shutil.rmtree(file)
        print(f"Contents of {file} has been deleted SUCCESSFULLY!")
    except OSError as e:
        print(f"Error! Directory: {file} : {e.strerror}")

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