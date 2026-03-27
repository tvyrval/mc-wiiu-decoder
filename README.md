# Minecraft Wii U Product Codes Decoder

A fast, lightweight Python script designed to decode the undocumented `WiiUProductCodes.bin` file used in **Minecraft: Wii U Edition**. It seamlessly parses both the older, dynamically padded legacy formats (like TU v64) and the natively sequential modern formats (like TU v688), extracting all structural DLC items into a clean, human-readable `.json` payload.

## Features

- **Format Adaptation**: Automatically detects backward-compatibility modes and deploys a byte-by-byte forward-scanning algorithm to safely bypass shifting alignment padding in legacy game files.
- **Cross-Region Consistency**: Natively detects and supports binaries formatted for European (`AUMP01`), American (`AUME01`), and Japanese (`AUMJ01`) game distributions.
- **Drag-and-Drop Native**: Built exclusively using standard Python tooling focused heavily on quality-of-life interface interactions on Windows (interactive paths via simple drag-and-drop mechanics).
- **Endianness Management**: Structurally accommodates the Wii U's native Big-Endian architecture integrated dynamically alongside C++ Little-Endian arrays without corruption.

## Usage

### 1. Simple Drag & Drop
Simply drag your `WiiUProductCodes.bin` file and drop it into the `decoder.py` terminal prompt when executed, or directly onto a Windows shortcut. The script will consume it instantly and emit the decoded results.

### 2. Command Line Execution
Alternatively, execute the script natively via command line by passing the binary's file path as an argument:
```cmd
python decoder.py "path/to/WiiUProductCodes.bin"
```

## Example Output Structure

The output extracts and preserves all known 32-bit parameters from the `WiiUProductCodes.bin` configuration:
```json
    {
        "index": 42,
        "name": "Festive Skin Pack",
        "short_name": "SPF",
        "product_id": 518,
        "code": "0010",
        "sort_index": 1667321888
    }
```

## Binary Documentation

If you are developing your own engine, a broader emulator infrastructure, or are interested in seeing *how* the hex structure maps internally inside the console itself, check out the provided [`WiiUProductCodes.md`](WiiUProductCodes.md) included in this repository for full technical formatting specifications.

---
*No external modules dependencies required. Strictly uses the Python standard library.*
