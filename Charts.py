import matplotlib.pyplot as plt
import seaborn as sns

def pie_chart(airports):
    top = airports['Country'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(top, labels=top.index, autopct='%1.1f%%',
           colors=sns.color_palette("Set2", 10))
    ax.set_title("Top 10 Countries by Airport Count",
                 fontsize=14, fontweight='bold')
    return fig

def histogram(airports):
    fig, ax = plt.subplots(figsize=(8, 5))
    airports['Altitude'].dropna().plot(
        kind='hist', bins=40,
        color='steelblue', edgecolor='white', ax=ax)
    ax.set_title("Distribution of Airport Altitudes",
                 fontsize=14, fontweight='bold')
    ax.set_xlabel("Altitude (feet)")
    ax.set_ylabel("Frequency")
    return fig

def line_chart(airports):
    tz = airports.groupby('Timezone').size().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    tz.plot(kind='line', marker='o', color='steelblue', ax=ax)
    ax.set_title("Airport Count by Timezone",
                 fontsize=14, fontweight='bold')
    ax.set_xlabel("Timezone (UTC Offset)")
    ax.set_ylabel("Number of Airports")
    return fig

def bar_chart(routes, airports):
    import pandas as pd
    merged = routes.merge(
        airports[['IATA', 'Country']],
        left_on='SrcAirport', right_on='IATA', how='left')
    top = merged['Country'].value_counts().head(15)
    fig, ax = plt.subplots(figsize=(10, 5))
    top.plot(kind='bar', color='steelblue', ax=ax)
    ax.set_title("Top 15 Countries by Number of Routes",
                 fontsize=14, fontweight='bold')
    ax.set_xlabel("Country")
    ax.set_ylabel("Route Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

def scatter_plot(airports):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(airports['Lon'], airports['Lat'],
               alpha=0.3, s=5, color='steelblue')
    ax.set_title("Global Airport Locations",
                 fontsize=14, fontweight='bold')
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    return fig

def box_plot(airports):
    data = airports[
        airports['DST'].isin(['E', 'A', 'S', 'O', 'Z', 'N'])
    ].dropna(subset=['Altitude'])
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.boxplot(x='DST', y='Altitude', data=data,
                palette='Blues', ax=ax)
    ax.set_title("Altitude by DST Category",
                 fontsize=14, fontweight='bold')
    ax.set_xlabel("DST Type")
    ax.set_ylabel("Altitude (feet)")
    return fig

def heatmap(airports):
    cols = ['Lat', 'Lon', 'Altitude', 'Timezone']
    corr = airports[cols].dropna().corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap='Blues', ax=ax)
    ax.set_title("Feature Correlation Heatmap",
                 fontsize=14, fontweight='bold')
    return fig

def area_chart(airports):
    tz = airports.groupby('Timezone').size().sort_index().cumsum()
    fig, ax = plt.subplots(figsize=(10, 5))
    tz.plot(kind='area', color='steelblue', alpha=0.5, ax=ax)
    ax.set_title("Cumulative Airports by Timezone",
                 fontsize=14, fontweight='bold')
    ax.set_xlabel("Timezone (UTC Offset)")
    ax.set_ylabel("Cumulative Count")
    return fig

def count_plot(airports):
    fig, ax = plt.subplots(figsize=(8, 5))
    order = airports['Type'].value_counts().index
    sns.countplot(x='Type', data=airports,
                  palette='Set2', order=order, ax=ax)
    ax.set_title("Airport Types Count",
                 fontsize=14, fontweight='bold')
    ax.set_xlabel("Type")
    ax.set_ylabel("Count")
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    return fig

def violin_plot(airports):
    data = airports[
        airports['DST'].isin(['E', 'A', 'S'])
    ].dropna(subset=['Altitude'])
    data = data[data['Altitude'] < 10000]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.violinplot(x='DST', y='Altitude',
                   data=data, palette='muted', ax=ax)
    ax.set_title("Altitude Distribution by DST (Violin)",
                 fontsize=14, fontweight='bold')
    return fig
