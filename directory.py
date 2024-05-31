import os

def directory(path):
    baseroot = os.path.expanduser('~\\Downloads\\Pytube')
    
    if not os.path.exists(baseroot):
        os.makedirs(baseroot)
    os.chdir(baseroot)
    
    if path in ["video", "audio", "playlist"]:
        path_dir = os.path.join(baseroot, path)
        
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        os.chdir(path_dir)
