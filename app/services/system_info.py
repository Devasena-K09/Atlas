import platform

def get_system_info():
    return {
        "platform": platform.system(),
        "processor": platform.processor()
    }