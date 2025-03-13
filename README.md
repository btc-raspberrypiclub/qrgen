# QR Code Generator with Logo - qrgen

A Python-based QR code generator that allows you to create QR codes with embedded logos and custom colors. This tool can be run using Docker, virtual environment, or as a standalone Python application.

## Prerequisites

For Docker:
- Docker installed on your system

For venv/standalone:
- Python 3.8 or higher
- pip (Python package installer)


## Getting Started

Clone the repository or download the source code:
```bash
git clone <repository-url-using-https-or-ssh>
cd qrgen
```

### Option 1: Docker Installation


Build the Docker image:
```bash
docker build -t qrgen .
```
Run the Docker image and generate default qr code: 
```bash
docker run -v $(pwd):/app qrgen python makeqr
```

### Option 2: Virtual Environment (recommended)

Create and activate a virtual environment:

On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

```bash
python makeqr
```

### Option 3: Standalone Installation

Install dependencies globally:
```bash
pip install -r requirements.txt
```

```bash
python makeqr
```

### Command Line Options

- `--logo`: Path to the logo image file (optional)
- `--url`: The URL or text to encode in the QR code (default: https://www.geeksforgeeks.org/)
- `--color`: The color of the QR code (default: Green)
- `--basewidth`: The base width of the logo image (default: 100)


### Usage Examples

The generated QR code will be saved in the current directory with the following naming convention:
- With logo: `{logo_name}_with_QR.png`
- Without logo: `qr_code_with_QR.png`

(If you are running Docker, prepend each of these with  `docker run -v $(pwd):/app qrgen` )

#### Generate a QR code with a custom URL and color:

```bash
python makeqr --url "https://example.com" --color "Blue"
```

#### Generate a QR code with a logo:

```bash
python makeqr --logo "logo.png" --url "https://example.com" --color "Red" --basewidth 150
```

### Running Tests

```bash
python -m unittest test_helpers.py -v
```

### License

GNU GENERAL PUBLIC LICENSE
