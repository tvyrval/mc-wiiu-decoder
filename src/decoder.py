import sys
import os
import struct
import json

def parse_wiiu_product_codes(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    pos = 0
    header_magic = data[pos:pos+12]
    pos += 12

    valid_magics = (b"AUMP01", b"AUME01", b"AUMJ01")
    if not header_magic.startswith(valid_magics):
        print("Warning: File magic does not match known Minecraft Wii U DLC prefixes (AUMP/E/J).")

    count = int.from_bytes(data[pos:pos+4], "little")
    pos += 4
    
    version = 0
    first_int = int.from_bytes(data[pos:pos+4], "little")
    if first_int == 0 and data[pos+4] < 0x80:
        version = 1
        unk1, unk2 = 0, 0
    else:
        unk1 = first_int
        pos += 4
        unk2 = int.from_bytes(data[pos:pos+4], "little")
        pos += 4
        if unk2 == 0:
            version = 2
        else:
            version = 3
    
    if version == 1:
        print(f"File Header (v1 Legacy) -> Count: {count}")
    elif version == 2:
        print(f"File Header (v2 Mid) -> Count: {count}, Unk1: {unk1}, Unk2: {unk2}")
    else:
        print(f"File Header (v3 Modern) -> Count: {count}, Unk1: {unk1}, Unk2: {unk2}")
    
    items = []
    
    for i in range(count):
        if pos >= len(data): break
        
        if version == 1 or version == 3:
            index_id = int.from_bytes(data[pos:pos+4], 'little')
            pos += 4
        else:
            index_id = i
        
        name_len = data[pos]
        pos += 1
        name = data[pos:pos+name_len].decode('ascii', errors='replace')
        pos += name_len
        
        if version == 1:
            unk_before_short = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            
            short_name_len = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            short_name = data[pos:pos+short_name_len].decode('ascii', errors='replace')
            pos += short_name_len
            
            p1 = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            p2 = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            p3 = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            
            product_id = p1 if p1 != 0 else (p2 if p2 != 0 else 0)
            
            item = {
                "index": index_id,
                "name": name,
                "short_name": short_name,
                "product_id": product_id,
                "dlc_type": unk_before_short,
                "unk_tail": [p1, p2, p3]
            }
            
            if i + 1 < count:
                for search_pos in range(pos, len(data) - 5):
                    candidate_id = int.from_bytes(data[search_pos:search_pos+4], 'little')
                    if 0 <= candidate_id < count and candidate_id not in [x["index"] for x in items]:
                        len_byte = data[search_pos+4]
                        if 0 < len_byte < 40:
                            test_str = data[search_pos+5:search_pos+5+min(3, len_byte)]
                            if all(32 <= b <= 126 for b in test_str):
                                pos = search_pos
                                break
        elif version == 2:
            short_name_len = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            short_name = data[pos:pos+short_name_len].decode('ascii', errors='replace')
            pos += short_name_len
            
            p1 = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            p2 = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            p3 = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            
            product_id = p1 if p1 != 0 else (p2 if p2 != 0 else 0)
            
            code = data[pos:pos+4].decode('ascii', errors='replace')
            pos += 4
            
            unk3 = int.from_bytes(data[pos:pos+4], 'little')
            pos += 4
            
            unk4 = int.from_bytes(data[pos:pos+4], 'little')
            pos += 4
            
            sort_index = int.from_bytes(data[pos:pos+4], 'little')
            pos += 4
            
            item = {
                "index": index_id,
                "name": name,
                "short_name": short_name,
                "product_id": product_id,
                "code": code,
                "unk3": unk3,
                "unk4": unk4,
                "sort_index": sort_index
            }
        else:
            short_name_len = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            short_name = data[pos:pos+short_name_len].decode('ascii', errors='replace')
            pos += short_name_len
            
            product_id = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            
            unk2_field = int.from_bytes(data[pos:pos+4], 'big')
            pos += 4
            
            code = data[pos:pos+4].decode('ascii', errors='replace')
            pos += 4
            
            unk3 = int.from_bytes(data[pos:pos+4], 'little')
            pos += 4
            
            unk4 = int.from_bytes(data[pos:pos+4], 'little')
            pos += 4
            
            sort_index = int.from_bytes(data[pos:pos+4], 'little')
            pos += 4
            
            item = {
                "index": index_id,
                "name": name,
                "short_name": short_name,
                "product_id": product_id,
                "unk2": unk2_field,
                "code": code,
                "unk3": unk3,
                "unk4": unk4,
                "sort_index": sort_index
            }
        
        items.append(item)
    
    return items

def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("WiiUProductCodes.bin Decoder")
        filepath = input("Drag and drop the WiiUProductCodes.bin file here and press Enter: ").strip('"').strip("'")
        
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        return

    print(f"Decoding file: {filepath}\n")
    try:
        items = parse_wiiu_product_codes(filepath)
    except Exception as e:
        print(f"Error decoding file: {e}")
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = os.path.basename(filepath) + ".json"
    output_file = os.path.join(script_dir, output_filename)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4)
        
    print(f"\nSuccessfully decoded {len(items)} items.")
    print(f"Output saved to: {output_file}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
