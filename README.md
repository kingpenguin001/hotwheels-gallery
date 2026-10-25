# Ruhaan's Garage

**Live gallery: https://kingpenguin001.github.io/hotwheels-gallery/**

This is Ruhaan's garage: his collection of Hot Wheels and other die-cast cars, every one photographed, named and rated by Ruhaan himself.

## The story

Ruhaan and I (Mandeep, his dad) both love Hot Wheels and little cars like them. What started as a few cars on the living-room floor has become a real collection, with favourites, duplicates and strong opinions about which ones deserve five stars.

I'm a software engineer, and this page is my version of a gift for him. Some dads build a shelf for their kid's cars; I built a website. I want it to be a treasure we can look back on years from now, and something that keeps him excited about a hobby we share. It isn't finished and never will be. It grows every time a new car joins the garage.

Ruhaan, keep collecting, keep racing, and keep this hobby alive. I'll keep building.

*With love, Papa*

## What's in the garage

- A guided intro from a 3D mini-Ruhaan who welcomes visitors and shows them how to use the filters (shown on the first visit; tap his face in the corner to replay it)
- Every car with its photo, brand and Ruhaan's star rating (1 to 5)
- Filters by brand (Hot Wheels, Majorette, Teamsterz, Dactoy) and by rating
- Search, plus sorting by rating, name, brand or the order the cars joined the collection
- A full-screen viewer: click any car, then use the arrow keys or swipe to browse
- Works on phones, tablets and big screens

## Adding new cars

The collection lives in a Google Drive folder: a spreadsheet (`Ruhaans Car Collection.xlsx` with columns Model, Brand, Rating, Quantity) and one photo per car.

1. Add the new car as a row in the spreadsheet and upload its photo to the folder. Name the photo with the brand prefix and that brand's next number, e.g. `HW-037.jpg` for the 37th Hot Wheels car (`MJ` = Majorette, `TS` = Teamsterz, `DC` = Dactoy).
2. Download the folder into `drive/` and rebuild:
   ```bash
   pip install gdown openpyxl pillow
   gdown --folder "<google-drive-folder-url>" -O drive
   python3 build_data.py      # resizes photos and regenerates cars.js / cars.json
   python3 build_single.py    # optional: one-file offline copy (ruhaans-car-collection.html)
   ```
3. Commit and push. GitHub Pages updates the live site within a minute or two.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The gallery page (plain HTML, CSS and JS, no frameworks) |
| `cars.js`, `cars.json` | Car data generated from the spreadsheet |
| `img/thumb/`, `img/full/` | Resized photos for the grid and the full-screen viewer |
| `build_data.py` | Turns the spreadsheet and photos into the files above |
| `build_single.py` | Builds a single self-contained HTML file to share offline |
