import wordcounts
import plotly, plotly.graph_objects as go

#plot histogram of word frequency for DHL
for s in wordcounts.wordListNoStopWordsdhl:
    x = [a for a in wordcounts.wordListNoStopWordsdhl]
    y = [wordcounts.wordListNoStopWordsdhl.count(p) for p in wordcounts.wordListNoStopWordsdhl]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Word Frequency for DHL",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Red")
fig.show()

# plot histogram of positive word frequency for DHL
for s in wordcounts.positiveWordListdhl:
    x = [a for a in wordcounts.positiveWordListdhl]
    y = [wordcounts.positiveWordListdhl.count(p) for p in wordcounts.positiveWordListdhl]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Positive Word Frequency for DHL",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Red")
fig.show()

# plot histogram of negative word frequency DHL
for s in wordcounts.negativeWordListdhl:
    x = [a for a in wordcounts.negativeWordListdhl]
    y = [wordcounts.negativeWordListdhl.count(p) for p in wordcounts.negativeWordListdhl]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Negative Word Frequency for DHL",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Red")
fig.show()

#plot histogram of word frequency for PosLaju
for s in wordcounts.wordListNoStopWordsposlaju:
    x = [a for a in wordcounts.wordListNoStopWordsposlaju]
    y = [wordcounts.wordListNoStopWordsposlaju.count(p) for p in wordcounts.wordListNoStopWordsposlaju]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Word Frequency for PosLaju",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Blue")
fig.show()

# plot histogram of positive word frequency for PosLaju
for s in wordcounts.positiveWordListposlaju:
    x = [a for a in wordcounts.positiveWordListposlaju]
    y = [wordcounts.positiveWordListposlaju.count(p) for p in wordcounts.positiveWordListposlaju]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Positive Word Frequency for PosLaju",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Blue")
fig.show()

# plot histogram of negative word frequency for PosLaju
for s in wordcounts.negativeWordListposlaju:
    x = [a for a in wordcounts.negativeWordListposlaju]
    y = [wordcounts.negativeWordListposlaju.count(p) for p in wordcounts.negativeWordListposlaju]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Negative Word Frequency for PosLaju",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Blue")
fig.show()

#plot histogram of word frequency for J&T
for s in wordcounts.wordListNoStopWordsjnt:
    x = [a for a in wordcounts.wordListNoStopWordsjnt]
    y = [wordcounts.wordListNoStopWordsjnt.count(p) for p in wordcounts.wordListNoStopWordsjnt]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Word Frequency for J&T",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Green") 
fig.show()

# plot histogram of positive word frequency for J&T
for s in wordcounts.positiveWordListjnt:
    x = [a for a in wordcounts.positiveWordListjnt]
    y = [wordcounts.positiveWordListjnt.count(p) for p in wordcounts.positiveWordListjnt]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Positive Word Frequency for J&T",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Green")
fig.show()

# plot histogram of negative word frequency for J&T
for s in wordcounts.negativeWordListjnt:
    x = [a for a in wordcounts.negativeWordListjnt]
    y = [wordcounts.negativeWordListjnt.count(p) for p in wordcounts.negativeWordListjnt]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Negative Word Frequency for J&T",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Green")
fig.show()

#plot histogram of word frequency for GDex
for s in wordcounts.wordListNoStopWordsgdex:
    x = [a for a in wordcounts.wordListNoStopWordsgdex]
    y = [wordcounts.wordListNoStopWordsgdex.count(p) for p in wordcounts.wordListNoStopWordsgdex]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Word Frequency for GDex",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Purple")
fig.show()

# plot histogram of positive word frequency for GDex
for s in wordcounts.positiveWordListgdex:
    x = [a for a in wordcounts.positiveWordListgdex]
    y = [wordcounts.positiveWordListgdex.count(p) for p in wordcounts.positiveWordListgdex]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Positive Word Frequency for GDex",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Purple")
fig.show()

# plot histogram of negative word frequency for GDex
for s in wordcounts.negativeWordListgdex:
    x = [a for a in wordcounts.negativeWordListgdex]
    y = [wordcounts.negativeWordListgdex.count(p) for p in wordcounts.negativeWordListgdex]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Negative Word Frequency for GDex",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Purple")
fig.show()

#plot histogram of word frequency for CityLink
for s in wordcounts.wordListNoStopWordscitylink:
    x = [a for a in wordcounts.wordListNoStopWordscitylink]
    y = [wordcounts.wordListNoStopWordscitylink.count(p) for p in wordcounts.wordListNoStopWordscitylink]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Word Frequency for CityLink",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Yellow")
fig.show()

# plot histogram of positive word frequency for CityLink
for s in wordcounts.positiveWordListcitylink:
    x = [a for a in wordcounts.positiveWordListcitylink]
    y = [wordcounts.positiveWordListcitylink.count(p) for p in wordcounts.positiveWordListcitylink]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Positive Word Frequency for CityLink",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Yellow")
fig.show()

# plot histogram of negative word frequency for CityLink
for s in wordcounts.negativeWordListcitylink:
    x = [a for a in wordcounts.negativeWordListcitylink]
    y = [wordcounts.negativeWordListcitylink.count(p) for p in wordcounts.negativeWordListcitylink]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Negative Word Frequency for CityLink",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    )
)
fig.update_traces(marker_color = "Yellow")
fig.show()