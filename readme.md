# Türkçe:

## Cross-Platform WiFi Password Finder

Bu proje, farklı işletim sistemlerinde WiFi şifrelerini bulan bir Python scripti içerir. Script, Windows, Linux ve macOS üzerinde çalışacak şekilde tasarlanmıştır ve SOLID prensiplerine uygun olarak yazılmıştır.

### Özellikler

- **Cross-Platform**: Windows, Linux ve macOS desteği.
- **SOLID Prensiplerine Uygun**: Kod modüler ve genişletilebilir.
- **Kolay Kullanım**: Script basit ve kullanımı kolaydır.

### Gereksinimler

- Python 3.x
- Gerekli Python paketleri: `subprocess`, `re`, `platform`, `abc`

### Kurulum

1. Bu projeyi yerel makinenize klonlayın veya indirin:
    ```sh
    https://github.com/abdulkadirtoklu4/Cross-Platform-Wifi-Password-Finder.git
    cd Cross-Platform-Wifi-Password-Finder
    ```

2. Gereksinimleri yükleyin:
    ```sh
    pip install -r requirements.txt
    ```

### Kullanım

1. Python scriptini çalıştırın:
    ```sh
    python3 main.py
    ```

2. Script, mevcut işletim sisteminizi algılar ve uygun yöntemi kullanarak WiFi şifrelerinizi ekrana yazdırır.

### Kod Yapısı

- `WifiPasswordFinder`: Abstract base class (ABC) olarak tanımlanmıştır ve işletim sistemine özgü sınıflar için bir arayüz sağlar.
- `WindowsWifiPasswordFinder`: Windows işletim sistemi için WiFi profillerini ve şifrelerini alır.
- `LinuxWifiPasswordFinder`: Linux işletim sistemi için WiFi profillerini ve şifrelerini alır.
- `MacOSWifiPasswordFinder`: macOS işletim sistemi için WiFi profillerini ve şifrelerini alır.
- `WifiPasswordService`: İşletim sistemine uygun `WifiPasswordFinder` sınıfını kullanarak tüm WiFi şifrelerini alır.

### SOLID Prensipleri

- **Single Responsibility Principle (SRP)**: Her sınıfın tek bir sorumluluğu vardır.
- **Open/Closed Principle (OCP)**: Yeni bir işletim sistemi desteği eklemek için mevcut kodu değiştirmeden yeni sınıflar eklenebilir.
- **Liskov Substitution Principle (LSP)**: `WifiPasswordFinder` arayüzünü implement eden her sınıf, `WifiPasswordService` tarafından kullanılabilir.
- **Interface Segregation Principle (ISP)**: `WifiPasswordFinder` arayüzü sadece gerekli metotları içerir.
- **Dependency Inversion Principle (DIP)**: `WifiPasswordService`, `WifiPasswordFinder` arayüzüne bağımlıdır, somut implementasyonlara değil.

### Geliştirme

Yeni bir işletim sistemi desteği eklemek için, `WifiPasswordFinder` arayüzünü implement eden yeni bir sınıf oluşturun ve `get_finder_for_current_os` fonksiyonuna ekleyin.

### Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

# English

## Cross-Platform WiFi Password Finder

This project contains a Python script that finds WiFi passwords across different operating systems. The script is designed to work on Windows, Linux, and macOS and is written according to SOLID principles.

### Features

- **Cross-Platform**: Supports Windows, Linux, and macOS.
- **SOLID Principles**: Modular and extensible code.
- **Easy to Use**: Simple and user-friendly script.

### Requirements

- Python 3.x
- Required Python packages: `subprocess`, `re`, `platform`, `abc`

### Installation

1. Clone or download this project to your local machine:
    ```sh
    git clone https://github.com/abdulkadirtoklu4/Cross-Platform-Wifi-Password-Finder.git
    cd Cross-Platform-Wifi-Password-Finder
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Run the Python script:
    ```sh
    python3 main.py
    ```

2. The script will detect your current operating system and print out the WiFi passwords using the appropriate method.

### Code Structure

- `WifiPasswordFinder`: Defined as an abstract base class (ABC) and provides an interface for OS-specific classes.
- `WindowsWifiPasswordFinder`: Retrieves WiFi profiles and passwords for Windows.
- `LinuxWifiPasswordFinder`: Retrieves WiFi profiles and passwords for Linux.
- `MacOSWifiPasswordFinder`: Retrieves WiFi profiles and passwords for macOS.
- `WifiPasswordService`: Uses the appropriate `WifiPasswordFinder` class for the current OS to retrieve all WiFi passwords.

### SOLID Principles

- **Single Responsibility Principle (SRP)**: Each class has a single responsibility.
- **Open/Closed Principle (OCP)**: New OS support can be added by creating new classes without modifying existing code.
- **Liskov Substitution Principle (LSP)**: Any class implementing the `WifiPasswordFinder` interface can be used by `WifiPasswordService`.
- **Interface Segregation Principle (ISP)**: The `WifiPasswordFinder` interface contains only necessary methods.
- **Dependency Inversion Principle (DIP)**: `WifiPasswordService` depends on the `WifiPasswordFinder` interface, not on concrete implementations.

### Development

To add support for a new operating system, create a new class that implements the `WifiPasswordFinder` interface and add it to the `get_finder_for_current_os` function.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
