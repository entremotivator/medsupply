import streamlit as st
import pandas as pd

# Sample data for the extended medical disposable product grid
data = {
    'Product Name': [
        'Disposable Poly Gown with Thumb Hooks', 'Disposable Underpads', 'Disposable Platinum Personal Care Towels',
        'Disposable Sterile Surgical Gown Blue', 'Disposable Isolation Gown', 'Disposable Lab Coat',
        'Disposable Medical Isolation Shoe Cover', 'Disposable Medical Cap Blue', 'Disposable Face Shield Anti-Fog Protection',
        'Disposable Toilet Seat Covers', 'Disposable Maternity Pads', 'Disposable Vinyl Gloves',
        'Disposable Medical Nitro / Chemo Gloves', 'Disposable Blue Nitro Gloves Force-Pro', 'Disposable KN95 Mask Black / White',
        'Disposable Sheer Strip Adhesive Bandages', 'Disposable Fabric Strip Adhesive Bandages', 'Disposable Sterile Gauze Pads',
        'Surgical Face Mask', 'Premoistened Adult Washcloths'
    ],
    'Category': ['Medical Disposables']*20,
    'SKU': [
        'SKU001', 'SKU002', 'SKU003', 'SKU004', 'SKU005', 'SKU006', 'SKU007', 'SKU008', 'SKU009', 'SKU010',
        'SKU011', 'SKU012', 'SKU013', 'SKU014', 'SKU015', 'SKU016', 'SKU017', 'SKU018', 'SKU019', 'SKU020'
    ],
    'Description': [
        'Full-body protection, thumb hooks for easy use', 'Waterproof underpads for patient beds', 'Super absorbent and soft towels',
        'Sterile gown for surgical procedures', 'Lightweight gown for patient protection', 'Disposable lab coat with full-length coverage',
        'Protects shoes in medical environments', 'Disposable medical cap for surgery or hygiene protection', 'Anti-fog face shield for full face protection',
        'Disposable sanitary toilet seat covers for public restrooms', 'Absorbent and soft maternity pads', 'Powder-free vinyl gloves for non-sterile environments',
        'Nitrile gloves with chemo protection', 'High-durability nitrile gloves for tough environments', 'KN95 mask with high filtration capacity',
        'Sheer strip adhesive bandages for minor wounds', 'Fabric strip bandages for extra flexibility', 'Sterile gauze pads for wound care',
        '3-ply surgical face mask for medical use', 'Disposable adult washcloths for patient care'
    ],
    'Specifications': [
        'Size: Universal; Material: Polypropylene', 'Size: 23x36 inches; Material: Soft cotton and polymer layers', 'Size: 24x24 inches; Material: Non-woven fabric',
        'Size: Universal; Sterility: Yes', 'Size: Universal; Material: Non-woven fabric', 'Size: Universal; Material: Non-woven fabric',
        'Size: Universal; Material: Polypropylene', 'Size: Universal; Color: Blue', 'Material: Polycarbonate; Coating: Anti-fog',
        'Pack: 50 covers; Material: Biodegradable paper', 'Size: Extra large; Absorption: High', 'Size: Medium; Material: Vinyl',
        'Size: Large; Material: Nitrile', 'Size: Large; Material: Nitrile', 'Colors: Black, White; Material: Multi-layer fabric',
        'Pack: 100 strips; Material: Plastic', 'Pack: 100 strips; Material: Fabric', 'Size: 4x4 inches; Sterility: Yes',
        'Size: One size; Layers: 3', 'Size: 8x12 inches; Material: Pre-moistened cloth'
    ],
    'Price': [
        '$14.99', '$9.99', '$19.99', '$29.99', '$9.99', '$12.99', '$6.99', '$3.99', '$5.99', '$3.50',
        '$7.99', '$12.99', '$15.99', '$16.99', '$19.99', '$3.99', '$4.50', '$7.50', '$12.99', '$9.99'
    ],
    'Available Stock': [
        '250 units', '500 packs', '300 packs', '150 units', '600 units', '400 units', '700 pairs', '1000 units', '500 units',
        '800 packs', '200 packs', '1000 packs', '500 boxes', '600 boxes', '800 packs', '1500 packs', '1200 packs', '700 packs',
        '1200 packs', '600 packs'
    ],
    'Link to Product': [
        'https://www.davismedstratum.com/...']*20,
    'Image Link': [
        'https://www.davismedstratum.com/...']*20
}

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Streamlit page configuration
st.set_page_config(page_title='Medical Disposables Product Grid', layout='wide')

# Streamlit title
st.title('Medical Disposables Product Grid')

# Display the DataFrame in a Streamlit table
st.write('Browse the extended product listings of medical disposables:')
st.dataframe(df)

# Optionally, add download functionality to allow users to download the product grid as a CSV
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(df)

st.download_button(
    label="Download product grid as CSV",
    data=csv_data,
    file_name='medical_disposables_product_grid.csv',
    mime='text/csv'
)

# Display product images based on the image links in the grid
st.write('Visualize some of the listed products:')
for index, row in df.iterrows():
    st.image(row['Image Link'], caption=row['Product Name'], use_column_width=True)

# Add product search functionality
st.write('Search for specific products by name:')
search_query = st.text_input('Enter product name:')
filtered_df = df[df['Product Name'].str.contains(search_query, case=False, na=False)]

# Show filtered results if a search query is provided
if not search_query:
    st.write('No search query entered. Displaying the entire product list.')
else:
    st.write(f'Showing results for "{search_query}":')
    st.dataframe(filtered_df)
