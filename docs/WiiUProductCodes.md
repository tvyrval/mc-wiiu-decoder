# WiiUProductCodes.bin Documentation

This document describes the structure of the `WiiUProductCodes.bin` file found in the game files of **Minecraft: Wii U Edition** (`content/WiiU/WiiUProductCodes.bin`). 

This binary file is used by the game interface to map internal DLCs (Skin Packs, Texture Packs, Mashup Packs) to their respective configuration names, sorting indexes, and eShop Product IDs.

Because the game engine uses a mix of generic C++ structures and Wii U (PowerPC) native objects, the file uses a chaotic mix of **Little-Endian (LE)** and **Big-Endian (BE)** values, alongside tightly packed Pascal strings.

---

## File Header

The file begins with a header containing a 12-byte region-specific magic string, followed by the number of item entries.

| Offset | Size (Bytes) | Type             | Description |
|--------|--------------|------------------|-------------|
| `0x00` | 12           | `char[12]`       | **Magic String**. Depends on the game's region:<br>- **EU**: `AUMP01D75\0\0\0`<br>- **US**: `AUME01D9D\0\0\0`<br>- **JP**: `AUMJ01DBE\0\0\0` |
| `0x0C` | 4            | `uint32_t` (LE)  | **Count**: The total number of DLC entries in the file. |

### Format Evolution
Due to the game's many updates across its lifespan, there are multiple revisions of this file. They broadly fall into three categories:
- **Older Formats**: The DLC entries begin immediately after the `Count` field (offset `0x10`).
- **Intermediate Formats**: The header has an additional 8 bytes before the entries begin. The entries lack a specific `Index ID`.
- **Newer Formats**: The header has an additional 8 bytes before the entries begin. The entries have an `Index ID`.

**Newer Format Additional Header Fields (Offset `0x10`):**
| Size | Type             | Description |
|------|------------------|-------------|
| 4    | `uint32_t` (LE)  | `Unk1` (Typically `1`). |
| 4    | `uint32_t` (LE)  | `Unk2` (Typically `1`). |

---

## Newer Format

In newer versions of the game, the DLC items are stored sequentially in an array. There is no structural padding between fields or entries; everything is tightly packed.

### Entry Structure
| Size | Type             | Endianness | Description |
|------|------------------|------------|-------------|
| 4    | `uint32_t`       | Little     | **Index ID**: Sequential integer (`0, 1, 2...`). |
| 1    | `uint8_t`        | -          | **Name Length**: Length of the following full name string. |
| Var. | `char[]`         | ASCII      | **Full Name**: The displayed name (e.g. `Festive Skin Pack`). |
| 4    | `uint32_t`       | Big        | **Short Name Length**: Length of the following code string. |
| Var. | `char[]`         | ASCII      | **Short Name / Abbreviation**: (e.g. `SPF`, `SPSI`). |
| 4    | `uint32_t`       | Big        | **Product ID**: The internal product ID / eShop ID for the DLC (e.g. `518`). |
| 4    | `uint32_t`       | Big        | **Unknown 2**: Variable configuration value. |
| 4    | `char[4]`        | ASCII      | **Code**: 4-character identifier string (e.g. `0010`). |
| 4    | `uint32_t`       | Little     | **Unknown 3**: Typically `0`. |
| 4    | `uint32_t`       | Little     | **Unknown 4**: Typically `1`. |
| 4    | `uint32_t`       | Little     | **Sort Index**: The priority index dictating where the DLC appears in UI menus. |

---

## Intermediate Format

Found in mid-generation updates (e.g., TU v161), this format serves as an evolutionary bridge between the old and new structures. It features the 8-byte header padding of the newer format and natively supports the `Code` strings and `Sort Index`, but uses the 12-byte tail block inherited from older formats, and uniquely omits the `Index ID` integers entirely.

### Entry Structure
| Size | Type             | Endianness | Description |
|------|------------------|------------|-------------|
| 1    | `uint8_t`        | -          | **Name Length**: Length of the full name string. *(Note: There is no preceding Index ID)* |
| Var. | `char[]`         | ASCII      | **Full Name**. |
| 4    | `uint32_t`       | Big        | **Short Name Length**. |
| Var. | `char[]`         | ASCII      | **Short Name / Abbreviation**. |
| 12   | `uint32_t[3]`    | Big        | **Tail Array**: Three 32-bit integers, logically identical to the Older Format tail block. |
| 4    | `char[4]`        | ASCII      | **Code**: 4-character identifier string (e.g. `0010`, or `----` for Bundles/Passes). |
| 4    | `uint32_t`       | Little     | **Unknown 3**: Typically `0`. |
| 4    | `uint32_t`       | Little     | **Unknown 4**: Typically `1`. |
| 4    | `uint32_t`       | Little     | **Sort Index**: The priority sorting index. |

---

## Older Format

Older versions of `WiiUProductCodes.bin` use a considerably different layout. The array is highly unoptimized: it lacks the `Code` strings entirely, injects arbitrary undocumented padding bytes between some entries, and shuffles the physical memory locations of the actual entries out-of-order (e.g. ID `16` appearing physically before ID `11`).

### Entry Structure
| Size | Type             | Endianness | Description |
|------|------------------|------------|-------------|
| 4    | `uint32_t`       | Little     | **Index ID**. |
| 1    | `uint8_t`        | -          | **Name Length**. |
| Var. | `char[]`         | ASCII      | **Full Name**. |
| 4    | `uint32_t`       | Big        | **DLC Type Identifier**: <br>`0` = Skin Packs<br>`1` = Texture Packs<br>`2` = Mashup Packs. |
| 4    | `uint32_t`       | Big        | **Short Name Length**. |
| Var. | `char[]`         | ASCII      | **Short Name / Abbreviation**. |
| 12   | `uint32_t[3]`    | Big        | **Tail Array**: Three 32-bit integers. The placement of the **Product ID** depends on the DLC Type (see below). |
| Var. | `byte[]`         | -          | **Padding**: Up to 6 bytes of padding exists between entries before the next `Index ID`. |

### Older Tail Array Map
Because the struct layout shifts dynamically depending on the DLC Type identifier, the 12-byte tail block behaves as follows:

- **Type `0` (Skin Packs)**: `[Product ID, 0, 8]`
- **Type `1` (Texture Packs)**: `[0, Product ID, 8]`
- **Type `2` (Mashup Packs)**: `[0, Product ID, 2]`

*(Note: "Festive Skin Pack" is an anomaly with a tail of `[0, 0, 1]`, and its product ID is 0.)* 

### Parsing Older Formats Robustly
Due to the varying and unpredictable alignment sizes and out-of-order `Index IDs`, the most robust way to extract older entries is to consume the 12-byte tail, then dynamically scan the hex forward byte-by-byte attempting to locate the next valid 4-byte `Index ID` integer.
