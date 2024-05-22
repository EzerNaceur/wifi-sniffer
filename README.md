# WiFi Sniffer

This Python program uses the Scapy library to sniff WiFi probe requests on a specified network interface. The interface to be sniffed is passed as an argument when running the program.

## Requirements

- Python 3.x
- Scapy library
- A wireless network interface that supports monitor mode

## Installation

1. **Install Scapy:**

    You can install Scapy using pip:

    ```bash
    pip install scapy
    ```

2. **Set the Wireless Interface to Monitor Mode:**

    To sniff WiFi packets, your wireless interface needs to be in monitor mode. The steps to enable monitor mode may vary depending on your operating system and wireless adapter. Below are the general steps for Linux:

    ```bash
    # Identify your wireless interface
    iwconfig

    # Bring the interface down
    sudo ifconfig <interface> down

    # Set the interface to monitor mode
    sudo iwconfig <interface> mode monitor

    # Bring the interface up
    sudo ifconfig <interface> up
    ```

    Replace `<interface>` with the name of your wireless interface (e.g., `wlan0`).

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/wifi-sniffer.git
    cd wifi-sniffer
    ```

2. **Run the Program:**

    ```bash
    python wifi-sniffer.py <interface>
    ```

    Replace `<interface>` with the name of your wireless interface (e.g., `wlan0`).

## Example

```bash
python wifi-sniffer.py wlan0
```
This command will start sniffing WiFi probe requests on the wlan0 interface.

##License

This project is licensed under the GNU general purpose License. See the LICENSE file for details.
