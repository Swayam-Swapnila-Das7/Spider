# Spider

Spider is a lightweight, web directory busting and reconnaissance tool inspired by dirb. Built in Python using the requests and sys modules, it automates URL fuzzing to discover hidden directories and files on a target web server. Developed as a hands-on project to master network protocols, HTTP status codes, and security tool development.

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Security Component](https://img.shields.io/badge/Field-Reconnaissance-red.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## ⚠️ LEGAL NOTICE & RESPONSIBLE USE

**THIS TOOL IS DESIGNED FOR AUTHORIZED SECURITY TESTING ONLY**

This tool performs directory enumeration and HTTP fuzzing on target web servers. **UNAUTHORIZED USE OF THIS TOOL ON SYSTEMS YOU DO NOT OWN OR HAVE NOT BEEN EXPLICITLY AUTHORIZED TO TEST IS ILLEGAL AND UNETHICAL.**

### Legitimate Use Cases:
- ✅ Penetration testing on your own infrastructure
- ✅ Authorized security assessments (with written permission)
- ✅ Educational purposes in controlled lab environments
- ✅ Capture The Flag (CTF) competitions
- ✅ Security research and training

### Prohibited Uses:
- ❌ Unauthorized access to computer systems
- ❌ Scanning third-party networks without permission
- ❌ Identifying vulnerabilities for malicious purposes
- ❌ Circumventing security measures on systems you don't own

---

## Installation

### Requirements:
- Python 3.10+
- pip (Python package manager)

### Setup Instructions (Recommended with Virtual Environment)

#### **Option 1: Using Virtual Environment (Recommended) 🔒**

Using a virtual environment is the best practice to isolate project dependencies and avoid conflicts with other Python projects.

**On Windows:**
```bash
# Clone the repository
git clone https://github.com/Swayam-Swapnila-Das7/Spider.git
cd Spider

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python spider.py
```

**On macOS/Linux:**
```bash
# Clone the repository
git clone https://github.com/Swayam-Swapnila-Das7/Spider.git
cd Spider

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python spider.py
```

#### **Option 2: Global Installation (Not Recommended)**

```bash
# Clone the repository
git clone https://github.com/Swayam-Swapnila-Das7/Spider.git
cd Spider

# Install dependencies globally
pip install -r requirements.txt

# Run the tool
python spider.py
```

---

## Usage

### Mode 1: Interactive CLI
```bash
python spider.py
```
Follow the on-screen prompts to enter the target URL and wordlist file path.

### Mode 2: Command Line Arguments
```bash
python spider.py <Target_URL> <Path_To_Wordlist>
```

Example:
```bash
python spider.py example.com common.txt
```

### Mode 3: Help
```bash
python spider.py help
# or
python spider.py -h
```

---

## Features

- 🎯 **Directory Enumeration**: Automated discovery of hidden directories and files
- 📊 **HTTP Status Categorization**: Distinguishes between successful, redirected, and error responses
- 🔐 **HTTPS Support**: Auto-enforces HTTPS protocol if missing
- 🎨 **Colored Output**: Clear, organized terminal output with color-coded results
- ⚡ **Lightweight**: Minimal dependencies and resource usage
- 🔧 **Flexible Input**: Support for wordlists with one entry per line

---

## Output Interpretation

| Status Code | Meaning | Output Color |
|---|---|---|
| 200-299 | Page Found | 🟢 Green |
| 300-399 | Redirect | 🟡 Yellow |
| 401, 403, 405 | Access Denied | 🔴 Red |
| 500+ | Server Error | 🔴 Red |

---

## Dependencies

See `requirements.txt` for detailed version information:
- `requests` - HTTP library for making requests
- `certifi` - SSL certificate verification
- `charset-normalizer` - Character encoding detection
- `idna` - International domain name support
- `urllib3` - HTTP client utilities

---

## Project Structure

```
Spider/
├── spider.py           # Main application script
├── requirements.txt    # Python dependencies
├── README.md          # Documentation
├── LICENSE            # MIT License with authorized use addendum
├── CODE_OF_CONDUCT.md # Responsible use guidelines
└── .gitignore         # Git ignore rules
```

---

## Author

**SWAYAM SWAPNILA DAS**
- GitHub: [@Swayam-Swapnila-Das7](https://github.com/Swayam-Swapnila-Das7)
- LinkedIn: [swayam-swapnila-das](https://www.linkedin.com/in/swayam-swapnila-das)

---

## License

This project is licensed under the **MIT License** with an important addition:

This software is provided for **authorized security testing purposes only**. Users are solely responsible for ensuring they have explicit permission before using this tool on any system or network. The author assumes no liability for misuse or unauthorized access.

See `LICENSE` for full license text.

---

## Code of Conduct

All users of this tool must adhere to the guidelines in `CODE_OF_CONDUCT.md`. By using this tool, you agree to:
- Use it only on systems you own or have permission to test
- Respect privacy and legal boundaries
- Report vulnerabilities responsibly
- Not use this tool for malicious purposes

---

## Professional Use & Ethical Framework

This project demonstrates commitment to ethical development:
- ✅ Comprehensive Code of Conduct
- ✅ Legal compliance guidelines
- ✅ Responsible disclosure principles
- ✅ Professional documentation standards

Used by security professionals and students for authorized testing 
and educational purposes only.

---

## Disclaimer

**USE AT YOUR OWN RISK.** This tool is provided as-is without any warranty. The author is not responsible for:
- Unauthorized access to computer systems
- Data loss or corruption
- Legal consequences arising from misuse
- System downtime or service disruptions

**By using this tool, you acknowledge that you understand and accept all risks associated with its use.**

---

## Virtual Environment FAQs

### What is a Virtual Environment?
A virtual environment is an isolated Python environment on your system. It allows you to install project-specific dependencies without affecting other projects or your system Python installation.

### Why Use Virtual Environment?
- ✅ **Isolation**: Each project has its own dependencies
- ✅ **No Conflicts**: Avoid version conflicts between projects
- ✅ **Clean System**: Keep your system Python clean
- ✅ **Best Practice**: Industry standard for Python development
- ✅ **Easy Cleanup**: Just delete the folder to remove all dependencies

### How to Deactivate Virtual Environment?
```bash
# On Windows
venv\Scripts\deactivate

# On macOS/Linux
deactivate
```

### How to Delete Virtual Environment?
```bash
# Simply delete the venv folder when done
rm -rf venv          # macOS/Linux
rmdir /s venv        # Windows
```

---

## Contributing

Contributions are welcome! Please ensure:
1. Your changes maintain the responsible use philosophy
2. You test thoroughly before submitting
3. You document your modifications
4. You adhere to the Code of Conduct

---

## Acknowledgments

- Inspired by [dirb](http://dirb.sourceforge.net/) - Directory enumeration tool
- Built with Python's `requests` library
- Part of the security community's commitment to ethical hacking practices

---

## Resources

- [OWASP - Authorized Testing](https://owasp.org/www-community/attacks/Web_Testing_Framework)
- [Legal Aspects of Penetration Testing](https://www.sans.org/reading-room/)
- [Responsible Disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Remember: With great power comes great responsibility. Use this tool ethically and legally.**
