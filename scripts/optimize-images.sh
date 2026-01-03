#!/bin/bash
for file in assets/images/**/*.{jpg,jpeg,png}; do
  if [ -f "$file" ]; then
    webp_file="${file%.*}.webp"
    if [ ! -f "$webp_file" ]; then
      echo "Converting $file to WebP..."
      cwebp -q 80 "$file" -o "$webp_file"
    fi
  fi
done
