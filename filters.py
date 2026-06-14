def apply_filters(airports, country=None, dst=None,
                  alt_min=None, alt_max=None,
                  search_text=None, airport_type=None):
    df = airports.copy()

    if country and country != "All":
        df = df[df['Country'] == country]

    if dst and dst != "All":
        df = df[df['DST'] == dst]

    if alt_min is not None:
        df = df[df['Altitude'] >= alt_min]

    if alt_max is not None:
        df = df[df['Altitude'] <= alt_max]

    if search_text:
        mask = (
            df['Name'].str.contains(search_text, case=False, na=False) |
            df['City'].str.contains(search_text, case=False, na=False)
        )
        df = df[mask]

    if airport_type and airport_type != "All":
        df = df[df['Type'] == airport_type]

    return df
