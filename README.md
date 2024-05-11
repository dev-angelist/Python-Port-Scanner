# Python Port Scanner

Python Port Scanner is a Python script that allows you to identify open ports on one or more specified IP addresses received as argument (via command line or file).


![image](https://github.com/dev-angelist/Python-Port-Scanner/assets/105108242/1c18de87-b48e-44b6-9a01-f676bd175021)


## Requirements

- Python 3.x
- pyfiglet library (installable via `pip install pyfiglet`)

## Download

On the repository page, click on the "Code" button located near the top-right corner. This will open a dropdown menu with a few options. Select "Download ZIP" to download the repository as a ZIP file. Or use following command via terminal:

```
git clone [https://github.com/username/repository.git](https://github.com/dev-angelist/Python-Port-Scanner)
```


## Usage

### Basic Example

To perform a port scan on a single IP address:

```
python3 port_scan.py -i 127.0.0.1
```

### Scanning Multiple IP Addresses

You can specify multiple IP addresses separated by commas or spaces:

```
python3 port_scan.py -i 127.0.0.1,192.168.1.1,10.0.0.1
```

### Scanning from File

You can specify IP addresses from a text file, with one address per line:

```
python3 port_scan.py -f ip_list.txt
```

The `ip_list.txt` file should contain IP addresses as follows:

```
127.0.0.1
192.168.1.1
10.0.0.1
```

### Specifying Output Directory

You can specify a directory to save output files containing the identified open ports:

```
python3 port_scan.py -i 127.0.0.1 -o output_directory
```

### Viewing Help

To display help with available options:

```
python3 port_scan.py -help
```

## Contributing

If you wish to contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch for your contribution (`git checkout -b feature/your-contribution`).
3. Commit your changes (`git commit -am 'Add feature X'`).
4. Push your branch (`git push origin feature/your-contribution`).
5. Open a pull request.

## Author

@dev-angelist ([GitHub profile](https://github.com/dev-angelist)) 


## Legal Disclaimer

Please note that conducting port scanning activities may be illegal in some jurisdictions without proper authorization. Before using this tool, ensure that you have the necessary permissions to perform scanning activities on the target network. Unauthorized port scanning can potentially violate laws and regulations related to computer security and privacy.

It is your responsibility to comply with all applicable laws and regulations in your jurisdiction. The author of this script does not condone or endorse any illegal or unauthorized use of this tool.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

--- 
