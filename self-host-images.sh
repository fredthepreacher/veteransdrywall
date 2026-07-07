#!/usr/bin/env bash
# Veteran Drywall — self-host the Wix-hotlinked images.
#
# Why this exists: the images on the live site are still hotlinked from
# static.wixstatic.com. That's a risk (breaks if the Wix plan is ever
# cancelled) and it's slower than serving from our own domain.
#
# Run this on a machine with normal internet access (this could NOT be run
# from inside the Claude session that wrote it — that sandbox's network is
# allowlisted and blocks static.wixstatic.com).
#
# Requirements: curl, and ImageMagick (`convert`) or cwebp for WebP output.
#   macOS:   brew install imagemagick webp
#   Ubuntu:  sudo apt-get install imagemagick webp
#
# Usage:
#   chmod +x self-host-images.sh
#   ./self-host-images.sh
#
# After running, update index.html: replace every static.wixstatic.com src
# with /assets/images/<filename>.webp (search for "static.wixstatic.com" —
# every occurrence has a TODO comment nearby marking what to change).

set -euo pipefail
OUT="assets/images"
mkdir -p "$OUT"

download_and_convert () {
  local url="$1" name="$2"
  echo "→ $name"
  curl -sL "$url" -o "$OUT/$name.src"
  if command -v cwebp >/dev/null 2>&1; then
    cwebp -q 85 "$OUT/$name.src" -o "$OUT/$name.webp"
  elif command -v convert >/dev/null 2>&1; then
    convert "$OUT/$name.src" -quality 85 "$OUT/$name.webp"
  else
    echo "  (no cwebp/imagemagick found — keeping original format only)"
    mv "$OUT/$name.src" "$OUT/$name.orig"
    return
  fi
  rm -f "$OUT/$name.src"
}

# Hero (also source for the 1200x630 og:image — crop/resize separately for social)
download_and_convert "https://static.wixstatic.com/media/e64608_65906d5cf39a407e832716c46caa1604~mv2.jpg/v1/fill/w_1600,h_1000,al_c,q_85/e64608_65906d5cf39a407e832716c46caa1604~mv2.jpg" "north-port-drywall-repair-hero"

# Why Us — owner photo
download_and_convert "https://static.wixstatic.com/media/e64608_6b4a976732a4444083bcff38d09b3f2d~mv2.jpeg/v1/crop/x_31,y_0,w_976,h_1464/fill/w_600,h_900,al_c,q_85/e64608_6b4a976732a4444083bcff38d09b3f2d~mv2.jpeg" "veteran-drywall-owner-steven-mcpherson"

# Gallery (8 images)
download_and_convert "https://static.wixstatic.com/media/e64608_cdfda03a4f6948f5bab48a8df4e4171d~mv2.jpeg/v1/fit/w_960,h_960,q_90/e64608_cdfda03a4f6948f5bab48a8df4e4171d~mv2.jpeg" "north-port-drywall-repair-project"
download_and_convert "https://static.wixstatic.com/media/e64608_78e9fe73a173465cac4988ad8c1ad8f7~mv2.jpeg/v1/fit/w_960,h_960,q_90/e64608_78e9fe73a173465cac4988ad8c1ad8f7~mv2.jpeg" "port-charlotte-texture-matching-project"
download_and_convert "https://static.wixstatic.com/media/e64608_58ca186cb9cb41db98441e75e91643d3~mv2.png/v1/fit/w_960,h_960,q_90/e64608_58ca186cb9cb41db98441e75e91643d3~mv2.png" "drywall-texture-matching-detail-closeup"
download_and_convert "https://static.wixstatic.com/media/e64608_2410a06b767d4f499e9cb0bae6638a55~mv2.png/v1/fit/w_960,h_960,q_90/e64608_2410a06b767d4f499e9cb0bae6638a55~mv2.png" "north-port-drywall-remodel-project"
download_and_convert "https://static.wixstatic.com/media/e64608_c2bdd0b4b08641f79dbd3b66a48d945e~mv2.jpeg/v1/fit/w_960,h_960,q_90/e64608_c2bdd0b4b08641f79dbd3b66a48d945e~mv2.jpeg" "drywall-installation-new-construction"
download_and_convert "https://static.wixstatic.com/media/e64608_5808502a2bc3433cbb114d5d7a08c541~mv2.jpeg/v1/fit/w_960,h_960,q_90/e64608_5808502a2bc3433cbb114d5d7a08c541~mv2.jpeg" "interior-paint-drywall-finish-work"
download_and_convert "https://static.wixstatic.com/media/e64608_d71299b1e4ef4169b25cfba0c351571f~mv2.jpeg/v1/fit/w_960,h_960,q_90/e64608_d71299b1e4ef4169b25cfba0c351571f~mv2.jpeg" "venice-fl-remodeling-project"
download_and_convert "https://static.wixstatic.com/media/e64608_85da5961321a4b1580295432f77a58dc~mv2.jpeg/v1/fit/w_960,h_960,q_90/e64608_85da5961321a4b1580295432f77a58dc~mv2.jpeg" "stucco-repair-exterior-charlotte-county"
download_and_convert "https://static.wixstatic.com/media/e64608_fe8282cedfc643fba95f606a19c3440e~mv2.jpeg/v1/fit/w_960,h_960,q_90/e64608_fe8282cedfc643fba95f606a19c3440e~mv2.jpeg" "drywall-ceiling-repair-charlotte-county"

# Team (3 images)
download_and_convert "https://static.wixstatic.com/media/e64608_87fe072f45714232a885f0d9cbcc2f9b~mv2.jpg/v1/crop/x_286,y_333,w_968,h_1346/fill/w_450,h_600,al_c,q_85/6C0A0926-Enhanced-NR-2.jpg" "veteran-drywall-team-steven"
download_and_convert "https://static.wixstatic.com/media/e64608_de52f63f0c9a4f7a9e53040ad5f8eec5~mv2.jpg/v1/crop/x_130,y_288,w_1074,h_1140/fill/w_450,h_600,al_c,q_85/6C0A0996-Enhanced-NR-2.jpg" "veteran-drywall-team-mike"
download_and_convert "https://static.wixstatic.com/media/e64608_57efbb2283754d0ba2eba70814b2673c~mv2.jpg/v1/crop/x_155,y_208,w_1112,h_1237/fill/w_450,h_600,al_c,q_85/6C0A1121-Enhanced-NR-2.jpg" "veteran-drywall-team-rick"

echo
echo "Done. Files are in $OUT/."
echo "Next: create a 1200x630 crop of the hero image for og:image (e.g. north-port-drywall-repair-social-share.jpg),"
echo "then update index.html — swap every static.wixstatic.com src for the matching /assets/images/<name>.webp path"
echo "and update og:image + the GeneralContractor schema 'image' field to the self-hosted social image."
