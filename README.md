# 🖼️ The Empire — Crew Image Optimizer

A production-ready Python utility created for **The Empire** website to optimize crew/member photographs for web use.

The project takes high-resolution images such as **PNG, JPG, JPEG, WebP, TIFF, BMP, HEIC and HEIF**, crops them to a consistent **3:4 portrait ratio**, resizes them to a web-friendly resolution, and converts them to **AVIF** format.

The original images are never modified.

---

## ✨ What Does This Project Do?

Crew photographs can often be several megabytes in size, especially when taken using modern phones or cameras.

For example:

```text
Original Image
     │
     │  3 MB PNG
     ▼
┌─────────────────────────┐
│  The Empire Optimizer   │
└─────────────────────────┘
     │
     ├── EXIF correction
     ├── 3:4 center crop
     ├── Resize to 1384 × 1840
     └── Convert to AVIF
     │
     ▼
Optimized Image
     │
     │  ~200–500 KB*
     ▼
Website
```

\*The final size depends on the original image and its visual complexity.

The goal is to significantly reduce website image size while keeping the photographs visually high quality.

---

# 🚀 Features

- ✅ PNG → AVIF
- ✅ JPG/JPEG → AVIF
- ✅ WebP → AVIF
- ✅ BMP → AVIF
- ✅ TIFF → AVIF
- ✅ HEIC → AVIF
- ✅ HEIF → AVIF
- ✅ Automatic 3:4 center cropping
- ✅ Resize to 1384 × 1840 pixels
- ✅ High-quality Lanczos resizing
- ✅ EXIF orientation correction
- ✅ Preserves original images
- ✅ Batch processing
- ✅ Automatic output directory creation
- ✅ Configurable AVIF quality
- ✅ Configurable overwrite behavior
- ✅ Displays compression statistics
- ✅ Continues processing if one image fails

---

# 📁 Project Structure

After downloading/cloning the project, the structure should look like this:

```text
The-Empire-Crew-Image-Optimizer/
│
├── convert_crew_images.py
├── requirements.txt
├── README.md
│
├── photos/
│   ├── member01.png
│   ├── member02.jpg
│   ├── member03.HEIC
│   └── ...
│
└── photos_avif/
    └──
```

> `photos_avif/` can be empty initially. The script will create it automatically if it does not exist.

---

# 💻 Requirements

You need:

- Python **3.9 or newer**
- pip
- The project files

Check whether Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

Check pip:

```bash
pip --version
```

---

# 📥 Installation

## 1. Clone the Repository

If you are using Git:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Then enter the project directory:

```bash
cd The-Empire-Crew-Image-Optimizer
```

If you downloaded the project as a ZIP file, extract it and open a terminal inside the extracted project folder.

---

## 2. Create a Virtual Environment

Creating a virtual environment is recommended so that the project's Python packages do not interfere with other Python projects.

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

After activation, you should see something similar to:

```text
(.venv)
```

at the beginning of your terminal prompt.

---

# 📦 3. Install Dependencies

The project includes a `requirements.txt` file containing all required Python packages.

Install everything with:

```bash
pip install -r requirements.txt
```

You do **not** need to install each package manually.

The requirements include:

```text
Pillow
pillow-avif-plugin
pillow-heif
```

These packages provide:

| Package | Purpose |
|---|---|
| `Pillow` | Image processing and resizing |
| `pillow-avif-plugin` | AVIF encoding support |
| `pillow-heif` | HEIC/HEIF image support |

---

# 📸 4. Add Your Images

Place all original crew/member photographs inside:

```text
photos/
```

Example:

```text
photos/
├── harshit.png
├── member02.jpg
├── member03.jpeg
├── member04.HEIC
└── member05.webp
```

You can mix different supported formats in the same folder.

---

# ⚙️ 5. Configure the Optimizer

Open:

```text
convert_crew_images.py
```

At the top of the file you will find configuration options similar to:

```python
INPUT_DIR = Path("photos")
OUTPUT_DIR = Path("photos_avif")

OUTPUT_WIDTH = 1384
OUTPUT_HEIGHT = 1840

AVIF_QUALITY = 90
AVIF_SPEED = 6

OVERWRITE = False
```

---

## Configuration Options

### Input Directory

```python
INPUT_DIR = Path("photos")
```

This is where the original photographs are located.

---

### Output Directory

```python
OUTPUT_DIR = Path("photos_avif")
```

This is where the optimized AVIF files will be created.

---

### Output Resolution

```python
OUTPUT_WIDTH = 1384
OUTPUT_HEIGHT = 1840
```

The resulting images use a **3:4 portrait ratio**.

```text
1384 ÷ 1840 ≈ 0.752
```

This resolution is intentionally larger than a 692 × 920 display size so that the images remain sharp on high-DPI displays.

---

### AVIF Quality

```python
AVIF_QUALITY = 90
```

The default quality is **90**, which is suitable for high-quality crew portraits.

General guidance:

```text
90  → Very high quality
85  → High quality
80  → Good quality
75  → Higher compression
```

For portrait photographs, a quality between **80–90** is generally recommended.

---

### AVIF Encoding Speed

```python
AVIF_SPEED = 6
```

This controls the encoding speed.

A higher value generally means faster encoding with potentially different compression efficiency.

The default value is intended to provide a practical balance between processing time and output size.

---

### Overwrite Existing Files

```python
OVERWRITE = False
```

When `False`, existing AVIF files are skipped.

For example:

```text
photos/
└── member01.png

photos_avif/
└── member01.avif
```

If `member01.avif` already exists, the script will not regenerate it.

To regenerate existing files:

```python
OVERWRITE = True
```

---

# ▶️ 6. Run the Optimizer

Once your images are inside the `photos/` directory, run:

```bash
python convert_crew_images.py
```

On some systems you may need:

```bash
python3 convert_crew_images.py
```

---

# 📊 7. What Happens When You Run It?

The script processes each image individually.

For every image, it:

1. Finds the image in `photos/`
2. Reads the image
3. Corrects its EXIF orientation
4. Converts it to a suitable color mode
5. Crops it to a 3:4 portrait ratio
6. Resizes it to 1384 × 1840 pixels
7. Encodes it as AVIF
8. Saves it inside `photos_avif/`
9. Reports the size difference

Conceptually:

```text
member01.png
      ↓
EXIF orientation correction
      ↓
3:4 center crop
      ↓
1384 × 1840 resize
      ↓
AVIF encoding
      ↓
member01.avif
```

---

# 📂 8. Where Are the Optimized Images?

After the script finishes, your project will look like:

```text
The-Empire-Crew-Image-Optimizer/
│
├── convert_crew_images.py
├── requirements.txt
├── README.md
│
├── photos/
│   ├── member01.png
│   ├── member02.jpg
│   └── member03.HEIC
│
└── photos_avif/
    ├── member01.avif
    ├── member02.avif
    └── member03.avif
```

The original images remain untouched.

---

# 🛡️ Original Images Are Safe

The optimizer does **not** replace your original images.

For example:

```text
photos/member01.png
```

remains exactly as it was.

The optimized version is created separately:

```text
photos_avif/member01.avif
```

This means you can always regenerate the AVIF files later using different quality settings.

---

# 🖼️ Image Quality

The optimizer is designed to reduce file size without unnecessarily degrading the visual quality of the photographs.

The process includes resizing and lossy AVIF compression, so the output will not be mathematically identical to the original.

However, with a quality setting such as:

```python
AVIF_QUALITY = 90
```

the resulting image should retain a high level of visual detail.

Always keep the original photographs as your master copies.

---

# 🌐 Using the Images on The Empire Website

After optimization, copy the generated `.avif` files into your website's image directory.

For example:

```text
public/
└── images/
    └── crew/
        ├── member01.avif
        ├── member02.avif
        └── member03.avif
```

Then update your crew data.

For example:

```json
{
  "id": "01",
  "name": "Member Name",
  "role": "Dancer",
  "image": "/images/crew/member01.avif"
}
```

The website can then load the optimized AVIF image instead of the original multi-megabyte PNG/JPG.

---

# ⚡ Why Optimize Images?

Suppose you have 30 crew photographs.

If every original photograph is approximately 3 MB:

```text
30 × 3 MB = 90 MB
```

Loading all of those large files directly would be inefficient for a website.

After optimization, if the average AVIF is around 300 KB:

```text
30 × 300 KB ≈ 9 MB
```

The actual result will depend on the photographs.

This can significantly reduce:

- Network transfer
- Page loading requirements
- Image decoding workload
- Storage requirements for web assets
- Mobile data usage

---

# 🎨 Why 3:4?

The Empire crew carousel uses portrait-style cards.

The optimizer therefore standardizes photographs to:

```text
Width  = 1384 px
Height = 1840 px
Ratio  = 3:4
```

This provides consistent framing across crew members.

---

# 📱 Why 1384 × 1840?

The website card can display the image at approximately:

```text
692 × 920 px
```

Using an output image around 2× that display size gives high-DPI devices additional pixels to work with.

Therefore:

```text
692 × 2 = 1384
920 × 2 = 1840
```

---

# 🔄 Re-running the Optimizer

You can safely run the script multiple times.

With:

```python
OVERWRITE = False
```

existing AVIF files are skipped.

If you change:

- Image quality
- Output resolution
- Cropping behavior
- Encoding settings

and want to regenerate everything, set:

```python
OVERWRITE = True
```

Then run:

```bash
python convert_crew_images.py
```

---

# 🧹 Cleaning the Output

If you want to completely regenerate the images, you can also remove the contents of:

```text
photos_avif/
```

and run:

```bash
python convert_crew_images.py
```

The original files inside `photos/` will remain untouched.

---

# 🐛 Troubleshooting

## Python is not recognized

If you see:

```text
'python' is not recognized...
```

make sure Python is installed and added to your system PATH.

Try:

```bash
py --version
```

On Windows, you can also run:

```bash
py convert_crew_images.py
```

---

## pip is not recognized

Try:

```bash
python -m pip install -r requirements.txt
```

instead of:

```bash
pip install -r requirements.txt
```

---

## HEIC files are not working

Make sure the dependencies are installed:

```bash
pip install -r requirements.txt
```

The project uses:

```text
pillow-heif
```

for HEIC/HEIF support.

---

## AVIF encoding error

Make sure the AVIF plugin is installed:

```bash
pip install pillow-avif-plugin
```

Or reinstall all dependencies:

```bash
pip install -r requirements.txt --upgrade
```

---

## Existing AVIF files are not changing

Check:

```python
OVERWRITE = False
```

Change it to:

```python
OVERWRITE = True
```

and run the script again.

---

# 📋 Quick Start

If you just want to run the project without reading all the documentation:

```bash
# 1. Clone/download the project

# 2. Enter the project
cd The-Empire-Crew-Image-Optimizer

# 3. Create virtual environment
python -m venv .venv

# 4. Activate it — Windows
.venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Put your images inside:
# photos/

# 7. Run the optimizer
python convert_crew_images.py
```

Your optimized images will be available in:

```text
photos_avif/
```

---

# 📦 Dependencies

The project uses the following Python packages:

```text
Pillow
pillow-avif-plugin
pillow-heif
```

They are listed in:

```text
requirements.txt
```

Install them all with:

```bash
pip install -r requirements.txt
```

---

# 🔧 Recommended Settings for The Empire

For crew portraits, the recommended configuration is:

```python
OUTPUT_WIDTH = 1384
OUTPUT_HEIGHT = 1840

AVIF_QUALITY = 90
AVIF_SPEED = 6

OVERWRITE = False
```

This provides a good balance between:

```text
Image Quality
      +
File Size
      +
Website Performance
```

---

# 🏛️ About The Project

This tool was created as part of **The Empire**, a college dance club website project.

The optimized images are intended for use in the website's crew/member carousel and other web components where portrait photographs are displayed.

**The Empire**

> Your Dance. Your Empire.

Website:

https://miet-the-empire.netlify.app/

---

# 📜 License

This project is intended for use with **The Empire** website/project.

The software code and the photographs are separate assets.

All photographs, personal images, logos, branding and other media remain the property of their respective owners.

Do not redistribute photographs without appropriate permission.
