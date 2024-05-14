import shutil, os, winshell, win32con, time

def delete_temp_files():
    folder = "C:\\WINDOWS\\Temp"

    shutil.rmtree(folder, ignore_errors=True)
    print(f"Contents of {folder} has been deleted SUCCESSFULLY!")

def delete_cache_file():
    folder = "C:\\WINDOWS\\SoftwareDistribution\\Download"
    local_app = os.getenv('LOCALAPPDATA')
    folder_user = os.path.join(local_app, 'Temp')
    
    try:
        if os.path.exists(folder):
            shutil.rmtree(folder, ignore_errors=True)
            print(f"Contents of {folder} has been deleted SUCCESSFULLY!")
        os.makedirs(folder)
        print(f"Recreated Directory: {folder}")
    except Exception as e:
        print(f"Failed to Process {folder} : Error: {e}")

    shutil.rmtree(folder_user, ignore_errors=True)
    print(f"Contents of {folder_user} has been deleted SUCCESSFULLY!")
    

def empty_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print(f"Recycle Bin has been emptied SUCCESSFULL!")
    except Exception as e:
        print(f"Error! Recycle Bin Not Emptied : Error: {e}")

def delete_old_downloads():
    folder = "C:\\Users\\user\\Downloads"
    current_time = time.time()
    day_limit = 30

    for (filename) in os.listdir(folder): 
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            file_age = (current_time - os.path.getctime(file_path) / (24*3600))
            if file_age > day_limit:
                os.remove(file_path)
                print(f"Deleted: {filename} from {folder}")
    print(f"Deleted All Files older than 30 Days from {folder}")
            
def delete_browser_cookies():
    shutil.rmtree(os.path.join(os.getenv("LOCALAPPDATA"), 'Google', 'Chrome', 'User Data', 'Default', 'Cache'))
    print(f"Browser Cookies and Cache Deleted SUCCESSFULLY!")

delete_temp_files()
delete_cache_file()
delete_browser_cookies()
empty_recycle_bin()
delete_old_downloads()