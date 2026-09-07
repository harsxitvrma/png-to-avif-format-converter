from pathlib import Path
from PIL import Image, ImageOps
import pillow_avif
import pillow_heif

pillow_heif.register_heif_opener()
# ============================================================
# THE EMPIRE — CREW IMAGE OPTIMIZER
# ============================================================

# ---------- CONFIGURATION ----------

INPUT_DIR = Path("photos")
OUTPUT_DIR = Path("photos_avif")

# Your website carousel is 692 × 920 (3:4)
# 2× resolution for high-DPI/Retina displays
OUTPUT_WIDTH = 1384
OUTPUT_HEIGHT = 1840

# 90 = very high visual quality
# Recommended for portraits where facial detail matters
AVIF_QUALITY = 90

# AVIF speed/quality tradeoff
# 0 = slowest/best compression
# 10 = fastest
AVIF_SPEED = 6

# Supported input formats
SUPPORTED_FORMATS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".bmp",
    ".tiff",
    ".heic",
    ".heif",
}

# Set True if you want to overwrite existing AVIF files
OVERWRITE = False


# ---------- FUNCTIONS ----------

def crop_to_3_4(image):
    """
    Center-crop image to exactly a 3:4 aspect ratio.
    """
    target_ratio = OUTPUT_WIDTH / OUTPUT_HEIGHT
    width, height = image.size
    current_ratio = width / height

    if current_ratio > target_ratio:
        # Image is too wide → crop width
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        image = image.crop(
            (left, 0, left + new_width, height)
        )

    elif current_ratio < target_ratio:
        # Image is too tall → crop height
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        image = image.crop(
            (0, top, width, top + new_height)
        )

    return image


def optimize_image(input_path, output_path):
    """
    Process one image:
    orientation → crop → resize → AVIF
    """

    with Image.open(input_path) as image:

        # Respect camera/phone EXIF orientation
        image = ImageOps.exif_transpose(image)

        original_size = image.size

        # Convert color mode
        # RGB is ideal for normal photographic portraits.
        if image.mode in ("RGBA", "LA"):
            # Preserve transparency if it exists
            image = image.convert("RGBA")
        else:
            image = image.convert("RGB")

        # Crop to exact 3:4 composition
        image = crop_to_3_4(image)

        # Resize to 1384 × 1840
        image = image.resize(
            (OUTPUT_WIDTH, OUTPUT_HEIGHT),
            Image.Resampling.LANCZOS
        )

        # Save as AVIF
        image.save(
            output_path,
            format="AVIF",
            quality=AVIF_QUALITY,
            speed=AVIF_SPEED
        )

    return original_size


def format_size(size_bytes):
    """
    Convert bytes into readable MB/KB.
    """
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"

    return f"{size_bytes / 1024:.1f} KB"


# ---------- MAIN ----------

def main():

    if not INPUT_DIR.exists():
        print(f"\n❌ Input folder not found:")
        print(f"   {INPUT_DIR.resolve()}")
        print("\nCreate the folder and put your crew photos inside it.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    files = [
        file
        for file in INPUT_DIR.iterdir()
        if file.is_file()
        and file.suffix.lower() in SUPPORTED_FORMATS
    ]

    if not files:
        print(f"\n⚠️ No supported images found in:")
        print(f"   {INPUT_DIR.resolve()}")
        return

    print("=" * 65)
    print("THE EMPIRE — CREW IMAGE OPTIMIZER")
    print("=" * 65)

    print(f"\nInput folder : {INPUT_DIR.resolve()}")
    print(f"Output folder: {OUTPUT_DIR.resolve()}")
    print(
        f"Output size  : "
        f"{OUTPUT_WIDTH} × {OUTPUT_HEIGHT} px (3:4)"
    )
    print(f"AVIF quality : {AVIF_QUALITY}")
    print(f"AVIF speed   : {AVIF_SPEED}")
    print(f"Images found : {len(files)}")

    print("\n" + "-" * 65)

    successful = 0
    skipped = 0
    failed = 0

    total_original = 0
    total_output = 0

    for index, input_path in enumerate(files, start=1):

        output_path = OUTPUT_DIR / f"{input_path.stem}.avif"

        # Don't overwrite unless explicitly enabled
        if output_path.exists() and not OVERWRITE:
            print(
                f"[{index:02d}/{len(files):02d}] "
                f"⏭️  SKIP: {input_path.name}"
            )
            skipped += 1
            continue

        try:
            original_bytes = input_path.stat().st_size

            original_dimensions = optimize_image(
                input_path,
                output_path
            )

            output_bytes = output_path.stat().st_size

            total_original += original_bytes
            total_output += output_bytes

            reduction = (
                (1 - output_bytes / original_bytes) * 100
                if original_bytes
                else 0
            )

            print(
                f"[{index:02d}/{len(files):02d}] "
                f"✅ {input_path.name}"
            )

            print(
                f"       "
                f"{original_dimensions[0]}×{original_dimensions[1]} "
                f"→ "
                f"{OUTPUT_WIDTH}×{OUTPUT_HEIGHT}"
            )

            print(
                f"       "
                f"{format_size(original_bytes)} "
                f"→ "
                f"{format_size(output_bytes)} "
                f"({reduction:.1f}% smaller)"
            )

            successful += 1

        except Exception as error:

            print(
                f"[{index:02d}/{len(files):02d}] "
                f"❌ FAILED: {input_path.name}"
            )

            print(f"       Error: {error}")

            failed += 1

    # ---------- SUMMARY ----------

    print("\n" + "=" * 65)
    print("CONVERSION COMPLETE")
    print("=" * 65)

    print(f"\n✅ Converted : {successful}")
    print(f"⏭️  Skipped   : {skipped}")
    print(f"❌ Failed    : {failed}")

    if successful > 0 and total_original > 0:

        total_reduction = (
            (1 - total_output / total_original) * 100
        )

        print("\nTOTAL SIZE:")
        print(
            f"   Original : {format_size(total_original)}"
        )
        print(
            f"   AVIF     : {format_size(total_output)}"
        )
        print(
            f"   Reduced  : {total_reduction:.1f}%"
        )

    print("\n📁 AVIF files saved to:")
    print(f"   {OUTPUT_DIR.resolve()}")

    print("\nDone.")


if __name__ == "__main__":
    main()