# Bing Daily Wallpaper Setter (Windows 11)

A lightweight Python script that automatically fetches the latest high-resolution daily wallpaper from Bing and sets it as your Windows 11 desktop background.

---

## 📌 Features
- **Bing API Integration**: Dynamically requests metadata for the latest wallpapers.
- **Random Selection**: Fetches up to 8 recent daily wallpapers and picks one at random upon execution.
- **Win32 API Binding**: Uses Python's native `ctypes` module to apply wallpapers instantly without external software.
- **Zero Dependencies**: Standard implementation relying on built-in modules (`requests`, `os`, `json`, `random`, `ctypes`).

---

## 🛠 Prerequisites & Installation

### Requirements
- Operating System: **Windows 10 / 11**
- Python 3.x
- `requests` library

### Installation
1. Clone or download this repository.
2. Install the required `requests` library if you haven't already:
   ```bash
   pip install requests
   ```

---

## 🚀 How to Run

Execute the script from your terminal or IDE:

```bash
python bing_wallpaper.py
```

Upon execution, the script will:
1. Fetch 8 recent wallpapers from Bing API.
2. Select a random image from the response.
3. Save the binary image data to `bing_wallpaper.jpg`.
4. Update your Windows desktop wallpaper immediately using the Win32 `user32.dll` API.

---

## 💻 Code Structure

- **`get_bing_wallpaper()`**: Queries Bing's JSON API, extracts the list of image objects, picks a random wallpaper, and constructs the full image URL.
- **`requests.get().content`**: Retrieves raw binary data for the selected wallpaper.
- **`os.path.abspath()`**: Resolves the full system path required by the Windows API.
- **`ctypes.windll.user32.SystemParametersInfoW()`**: Invokes `SPI_SETDESKWALLPAPER` (code `20`) to immediately force Windows to set the new background and write to registry (`SPIF_UPDATEINIFILE | SPIF_SENDCHANGE`).

---

## ⏰ Auto-run on Startup (Optional)

To automatically change your wallpaper every time you boot Windows 11:

1. Press `Win + R`, type `shell:startup`, and press **Enter**.
2. Create a shortcut to your `bing_wallpaper.py` script (or a `.bat` file that runs `python path\to\bing_wallpaper.py`) inside this folder.