import subprocess
import re
import platform
from abc import ABC, abstractmethod

class WifiPasswordFinder(ABC):
    @abstractmethod
    def get_profiles(self):
        pass
    
    @abstractmethod
    def get_password(self, profile):
        pass

class WindowsWifiPasswordFinder(WifiPasswordFinder):
    def get_profiles(self):
        wifi_profiles = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
        return re.findall("All User Profile\s*:\s*(.*)", wifi_profiles.stdout)
    
    def get_password(self, profile):
        profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True)
        password = re.search("Key Content\s*:\s*(.*)", profile_info.stdout)
        return password.group(1) if password else None

class LinuxWifiPasswordFinder(WifiPasswordFinder):
    def get_profiles(self):
        wifi_profiles = subprocess.run(['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'], capture_output=True, text=True)
        return re.findall('yes:(.*)', wifi_profiles.stdout)
    
    def get_password(self, profile):
        profile_info = subprocess.run(['sudo', 'grep', '^psk=', f'/etc/NetworkManager/system-connections/{profile}.nmconnection'], capture_output=True, text=True)
        password = re.search('^psk=(.*)', profile_info.stdout)
        return password.group(1) if password else None

class MacOSWifiPasswordFinder(WifiPasswordFinder):
    def get_profiles(self):
        wifi_profiles = subprocess.run(['/usr/sbin/networksetup', '-listpreferredwirelessnetworks', 'en0'], capture_output=True, text=True)
        return re.findall(r'(\w[\w\s]+\w)', wifi_profiles.stdout)
    
    def get_password(self, profile):
        profile_info = subprocess.run(['security', 'find-generic-password', '-D', 'AirPort network password', '-a', profile, '-w'], capture_output=True, text=True)
        return profile_info.stdout.strip() if profile_info.returncode == 0 else None

class WifiPasswordService:
    def __init__(self, finder: WifiPasswordFinder):
        self.finder = finder

    def get_all_passwords(self):
        wifi_details = {}
        profiles = self.finder.get_profiles()
        for profile in profiles:
            wifi_details[profile] = self.finder.get_password(profile)
        return wifi_details

def get_finder_for_current_os():
    current_os = platform.system()
    if current_os == 'Windows':
        return WindowsWifiPasswordFinder()
    elif current_os == 'Linux':
        return LinuxWifiPasswordFinder()
    elif current_os == 'Darwin':
        return MacOSWifiPasswordFinder()
    else:
        raise NotImplementedError(f"{current_os} is not supported")

if __name__ == "__main__":
    finder = get_finder_for_current_os()
    service = WifiPasswordService(finder)
    wifi_passwords = service.get_all_passwords()
    for profile, password in wifi_passwords.items():
        if password:
            print(f"SSID Name: {profile}, Password: {password}")
        else:
            print(f"SSID Name: {profile}, Password Not Found.")
