import struct
import zlib

def create_png(width, height, bg_color, accent_color, size_label):
    """Create a minimal PNG with GainSzn branding."""
    def png_pack(data):
        return zlib.compress(data)

    # Create pixel data
    pixels = []
    cx, cy = width // 2, height // 2

    for y in range(height):
        row = []
        for x in range(width):
            # Background: black
            r, g, b = 10, 10, 10

            # Red circle accent
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            radius = min(width, height) * 0.38
            inner = radius * 0.6

            if dist <= radius and dist >= inner:
                r, g, b = 204, 0, 0  # #CC0000

            # G letter in center (simplified pixel art)
            gw = width * 0.22
            gh = height * 0.30
            gx = cx - gw * 0.5
            gy = cy - gh * 0.5
            stroke = max(2, width // 30)

            # G shape
            in_g = False
            # Top bar
            if gx <= x <= gx + gw and gy <= y <= gy + stroke:
                in_g = True
            # Bottom bar
            if gx <= x <= gx + gw and gy + gh - stroke <= y <= gy + gh:
                in_g = True
            # Left bar
            if gx <= x <= gx + stroke and gy <= y <= gy + gh:
                in_g = True
            # Right bar (bottom half only)
            if gx + gw - stroke <= x <= gx + gw and gy + gh * 0.5 <= y <= gy + gh:
                in_g = True
            # Middle bar
            if gx + gw * 0.5 <= x <= gx + gw and cy - stroke * 0.5 <= y <= cy + stroke * 0.5:
                in_g = True

            if in_g:
                r, g, b = 255, 255, 255

            row.extend([r, g, b])
        pixels.append(row)

    def make_png_bytes(pixels, width, height):
        def pack_chunk(chunk_type, data):
            chunk_len = struct.pack('>I', len(data))
            chunk_data = chunk_type + data
            chunk_crc = struct.pack('>I', zlib.crc32(chunk_data) & 0xffffffff)
            return chunk_len + chunk_data + chunk_crc

        # PNG signature
        sig = b'\x89PNG\r\n\x1a\n'

        # IHDR
        ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
        ihdr = pack_chunk(b'IHDR', ihdr_data)

        # IDAT
        raw = b''
        for row in pixels:
            raw += b'\x00' + bytes(row)
        compressed = zlib.compress(raw, 9)
        idat = pack_chunk(b'IDAT', compressed)

        # IEND
        iend = pack_chunk(b'IEND', b'')

        return sig + ihdr + idat + iend

    return make_png_bytes(pixels, width, height)

for size in [192, 512]:
    data = create_png(size, size, (10, 10, 10), (204, 0, 0), str(size))
    with open(f'/home/user/gainszn/icons/icon-{size}x{size}.png', 'wb') as f:
        f.write(data)
    print(f'Created icon-{size}x{size}.png ({len(data)} bytes)')

print('Icons generated.')
